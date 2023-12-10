import uuid
from flask import Flask, app, request, jsonify, Blueprint, render_template, session, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, validators
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from apps.model.model import Favorite, Recipe, Ingredient, User
from apps import db
import json, os

bp = Blueprint("recipe", __name__, url_prefix="/api")

@bp.route("/get_recipe", methods=["GET"])
def get_recipe():
    type = request.args.get("type")
    cplist = []
    # Get the list of recipes from database
    recipe_objs = Recipe.query.all()
    for recipe in recipe_objs:
        # Identify type of recipe
        if type == recipe.type or type == 'all':
            recipedata = {}
            recipedata['id'] = recipe.id
            recipedata['name'] = recipe.name
            recipedata['path'] = recipe.path
            cplist.append(recipedata)
    context = {
        "cplist": cplist,
        "recipe_type": type
        }
    return render_template("recipe.html", **context)


@bp.route("/get_posted_recipe", methods=["GET"])
def get_posted_recipe():
    user_id = session["logged_in"]
    user_recipes = Recipe.query.filter_by(user_id=user_id).all()

    cplist = []
    for recipe in user_recipes:
        recipedata = {
            "id": recipe.id,
            "name": recipe.name,
            "path": recipe.path
        }
        cplist.append(recipedata)

    context = {"cplist": cplist}

    return render_template("view_posted.html", **context)


@bp.route("/recipe_detail/<int:recipe_id>", methods=["GET"])
def recipe_detail(recipe_id):
    # Get the details of the selected recipe from the database
    recipe = Recipe.query.get(recipe_id) 

    # Check if the current user has already favorited this recipe
    is_favorited = False
    if session.get('logged_in'):
        user_id = session['logged_in']
        is_favorited = Favorite.query.filter_by(user_id=user_id, recipe_id=recipe_id).first() is not None

    context = {
        "recipe": {
            "id" : recipe.id,
            "name": recipe.name,
            "path": recipe.path,
            "type": recipe.type,
            "description": recipe.description,
            "ingredients": recipe.ingredients,
            "is_favorited": is_favorited
        },
    }

    return render_template("recipe_detail.html", **context)

class RecipeForm(FlaskForm):
    recipe_name = StringField('name', validators=[validators.DataRequired()])
    recipe_image = FileField('image', validators=[FileRequired()])
    recipe_type = SelectField('type', choices=[('eastern', 'Eastern'), ('western', 'Western')],
                              validators=[validators.DataRequired()])

@bp.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if session.get('logged_in'):
        user_id = session.get('logged_in')
        if request.method == 'POST':
            # Get data
            recipe_name = request.form.get('recipe_name')
            recipe_type = request.form.get('type')
            recipe_description = request.form.get('recipe_context')
            recipe_image = request.form.get('imagepath')

            ingredients = request.form.getlist('ingredient[]')
            amounts = request.form.getlist('amount[]')

            # Save recipe data to the database
            new_recipe = Recipe(user_id=user_id, name=recipe_name, path=recipe_image,
                                type=recipe_type, description=recipe_description)
            db.session.add(new_recipe)
            db.session.commit()

            # Save ingredient data to database
            recipe_id = new_recipe.id
            for ingredient, amount in zip(ingredients, amounts):
                new_ingredient = Ingredient(
                    recipe_id=recipe_id, name=ingredient, amount=amount)
                db.session.add(new_ingredient)
                db.session.commit()

            flash('Recipe added successfully!', 'success')
            return redirect(url_for('recipe.recipe_detail', recipe_id=recipe_id))
        return render_template("add_recipe.html")
    return "please log in"


@bp.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(str(uuid.uuid4()) + '_' + f.filename)
        basepath = os.getcwd()
        upload_path = os.path.join(
            basepath, r'apps\static\image\recipes', filename)
        f.save(upload_path)
        return {'msg': 'ok', 'filename': r'/static/image/recipes/'+ filename}


@bp.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword")
    search_type = request.args.get("search_type")
    cplist = []
    if search_type == "all":
        recipe_type = request.args.get("recipe_type")
        print("Using specific recipe type:", recipe_type)
        # Search in all recipes
        if recipe_type in ["eastern", "western"]:
            recipe_objs = Recipe.query.filter(
                Recipe.name.ilike(f'%{keyword}%'),
                Recipe.type == recipe_type
            ).all()
        else:
            recipe_objs = Recipe.query.filter(
                Recipe.name.ilike(f'%{keyword}%')
            ).all()
    elif search_type == "posted":
        # Search in posted recipes
        user_id = session.get("logged_in")
        recipe_objs = Recipe.query.filter(
            Recipe.user_id == user_id,
            Recipe.name.ilike(f'%{keyword}%')
        ).all()
    elif search_type == "favorited":
        # Search in favorited recipes
        user_id = session.get("logged_in")
        favorite_recipe_ids = [fav.recipe_id for fav in Favorite.query.filter_by(user_id=user_id).all()]
        recipe_objs = Recipe.query.filter(
            Recipe.id.in_(favorite_recipe_ids),
            Recipe.name.ilike(f'%{keyword}%')
        ).all()

    for recipe in recipe_objs:
        recipedata = {"id": recipe.id, "name": recipe.name, "path": recipe.path}
        cplist.append(recipedata)

    return cplist

  
@bp.route("/get_favorite", methods=["GET"])
def get_favorite():
    # Get the user's ID
    user_id = session['logged_in']

    # Query the favorites for the current user
    favorites = Favorite.query.filter_by(user_id=user_id).all()

    cplist = []
    for favorite in favorites:
        # Retrieve the details of the favorited recipe
        recipe = Recipe.query.get(favorite.recipe_id)
        
        # Add recipe details to the list
        recipedata = {
            "id": recipe.id,
            "name": recipe.name,
            "path": recipe.path,
            "type": recipe.type,
            "description": recipe.description,
            "ingredients": recipe.ingredients
        }
        cplist.append(recipedata)

    context = {
        "cplist": cplist
    }
    
    return render_template("favorite.html", **context)


@bp.route("/favorite/<int:recipe_id>", methods=["POST"])
def favorite_recipe(recipe_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    user_id = session.get('logged_in')
    favorite = Favorite(user_id=user_id, recipe_id=recipe_id)
    db.session.add(favorite)
    db.session.commit()

    flash('Recipe added to favorites!', 'success')
    return redirect(url_for('recipe.recipe_detail', recipe_id=recipe_id))


@bp.route("/unfavorite/<int:recipe_id>", methods=["POST"])
def unfavorite_recipe(recipe_id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))

    user_id = session.get('logged_in')
    favorite = Favorite.query.filter_by(user_id=user_id, recipe_id=recipe_id).first()
    if favorite:
        db.session.delete(favorite)
        db.session.commit()
        flash('Recipe removed from favorites!', 'success')

    return redirect(url_for('recipe.recipe_detail', recipe_id=recipe_id))
