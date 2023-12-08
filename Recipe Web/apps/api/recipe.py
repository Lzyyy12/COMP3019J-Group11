import uuid
from flask import Flask, app, request, jsonify, Blueprint, render_template, session, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, validators
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from apps.model.model import Recipe
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
            recipedata['name'] = recipe.name
            recipedata['path'] = recipe.path
            cplist.append(recipedata)
   
    context = {
        "cplist": cplist
        }
    
    return render_template("recipe.html", **context)

class RecipeForm(FlaskForm):
    recipe_name = StringField('name', validators=[validators.DataRequired()])
    recipe_image = FileField('image', validators=[FileRequired()])
    recipe_type = SelectField('type', choices=[('eastern', 'Eastern'), ('western', 'Western')],
                              validators=[validators.DataRequired()])

@bp.route("/edit_recipe", methods=["GET", "POST"])
def edit_recipe():
    if session.get('logged_in'):
        if request.method == 'POST':
            recipe_name = request.form.get('recipe_name')
            recipe_type = request.form.get('recipe_type')

            # Get the image file
            recipe_image = request.files['recipe_image']

            # Give the image an unique filename
            filename = str(uuid.uuid4()) + '_' + recipe_image.filename

            # Save the image to system
            basepath = os.getcwd()
            upload_path = os.path.join(basepath, 'Recipe Web/apps/static/image/recipes', filename)
            save_path = os.path.join('../static/image/recipes', filename)
            recipe_image.save(upload_path)

            # Save data to the database
            new_recipe = Recipe(name=recipe_name, path=save_path, type=recipe_type)
            db.session.add(new_recipe)
            db.session.commit()

            flash('Recipe added successfully!', 'success')
            return redirect("/")
        return render_template("edit_recipe.html")
    return "please log in"

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

@bp.route("/view_recipe", methods=["GET"])
def view_recipe():
    type = request.args.get("type")
    cplist = []
    # Get the list of recipes from database
    recipe_objs = Recipe.query.all()
    for recipe in recipe_objs:
        # Identify type of recipe
        if type == recipe.type or type == 'all':
            recipedata = {}
            recipedata['name'] = recipe.name
            recipedata['path'] = recipe.path
            cplist.append(recipedata)
   
    context = {
        "cplist": cplist
        }
    
    return render_template("recipe.html", **context)

@bp.route("/get_favorite", methods=["GET"])
def get_favorite():
    type = request.args.get("type")
    cplist = []
    # Get the list of recipes from database
    recipe_objs = Recipe.query.all()
    for recipe in recipe_objs:
        # Identify type of recipe
        if type == recipe.type or type == 'all':
            recipedata = {}
            recipedata['name'] = recipe.name
            recipedata['path'] = recipe.path
            cplist.append(recipedata)
   
    context = {
        "cplist": cplist
        }
    
    return render_template("recipe.html", **context)