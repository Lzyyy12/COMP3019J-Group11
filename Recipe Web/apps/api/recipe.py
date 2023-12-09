import uuid
from flask import Flask, app, request, jsonify, Blueprint, render_template, session, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, validators
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from apps.model.model import Recipe, Ingredient
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
        "cplist": cplist
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

    context = {
        "recipe": {
            "name": recipe.name,
            "path": recipe.path,
            "type": recipe.type,
            "description": recipe.description,
            "ingredients": recipe.ingredients
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
                    recipe_id=recipe_id, user_id=user_id, name=ingredient, amount=amount)
                db.session.add(new_ingredient)
                db.session.commit()

            flash('Recipe added successfully!', 'success')
            return redirect("/api/get_recipe?type=all")
        return render_template("add_recipe.html")
    return "please log in"


@bp.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.getcwd()
        upload_path = os.path.join(
            basepath, r'apps\static\image\recipes', f.filename)
        f.save(upload_path)
        return {'msg': 'ok', 'filename': r'/static/image/recipes/'+f.filename}


@bp.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword")
    cplist = []
    # Get the list of recipes from database
    recipe_objs = Recipe.query.filter(Recipe.name.ilike(
        '%{keyword}%'.format(keyword=keyword))).all()
    for recipe in recipe_objs:
        recipedata = {}
        recipedata['name'] = recipe.name
        recipedata['path'] = recipe.path
        cplist.append(recipedata)

    return cplist


@bp.route("/view_posted", methods=["GET"])
def view_posted():
    cplist = []
   
    context = {
        "cplist": cplist
        }
    
    return render_template("view_posted.html", **context)


@bp.route("/get_favorite", methods=["GET"])
def get_favorite():
    cplist = []
   
    context = {
        "cplist": cplist
        }
    
    return render_template("favorite.html", **context)