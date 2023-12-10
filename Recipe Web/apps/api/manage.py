import uuid
from flask import Flask, app, request, jsonify, Blueprint, render_template, session, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, validators
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from apps.model.model import User, Recipe, Ingredient
from apps import db
import json, os

bp = Blueprint("manage", __name__, url_prefix="/api")

@bp.route("/manage_user", methods=["GET"])
def manage_user():
    cplist = []
    # Get the list of users from database
    user_objs = User.query.all()
    for user in user_objs:
        userdata = {}
        userdata['id'] = user.id
        userdata['name'] = user.name
        userdata['photo'] = user.photo
        cplist.append(userdata)
   
    context = {
        "cplist": cplist
        }
    
    return render_template("manage_user.html", **context)

@bp.route("/delete_user", methods=["POST"])
def delete_user():
    userId = request.form['userId']
    del_count = db.session.query(User).filter(User.id == userId).delete()
    db.session.commit()
    if del_count == 1 :
        return "delete succeeded"
    return "delete failed"


@bp.route("/manage_recipe", methods=["GET"])
def manage_recipe():
    cplist = []
    # Get the list of recipes from database
    recipe_objs = Recipe.query.all()
    for recipe in recipe_objs:
        recipedata = {}
        recipedata['id'] = recipe.id
        recipedata['name'] = recipe.name
        recipedata['path'] = recipe.path
        cplist.append(recipedata)

    context = {
        "cplist": cplist
    }
    return render_template("manage_recipe.html", **context)


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


@bp.route("/manage_edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def manage_edit_recipe(recipe_id):
    if session.get('logged_in'):
        if request.method == 'POST':
            # Get data
            recipe_name = request.form.get('recipe_name')
            recipe_type = request.form.get('type')
            recipe_description = request.form.get('recipe_context')
            recipe_image = request.form.get('imagepath')

            ignames = request.form.getlist('ignames')
            igamounts = request.form.getlist('igamounts')

            # Save recipe data to the database
            new_recipe = Recipe.query.filter_by(id=recipe_id) .first()
            new_recipe.user_id = session.get('logged_in')
            new_recipe.name = recipe_name
            new_recipe.path = recipe_image
            new_recipe.type = recipe_type
            new_recipe.description = recipe_description
            db.session.commit()

            Ingredient.query.filter(recipe_id == recipe_id).delete()
            db.session.commit()
            for name, amount in zip(ignames, igamounts):
                new_ingredient = Ingredient(
                    recipe_id=recipe_id, name=name, amount=amount)
                db.session.add(new_ingredient)
                db.session.commit()

            flash('Recipe added successfully!', 'success')
            # return redirect("/")
            return redirect("/api/manage_recipe")
        else:
            recipe = Recipe.query.get(recipe_id)
            # ingredients = recipe.ingredients

            context = {
                "recipe": {
                    "id": recipe.id,
                    "name": recipe.name,
                    "path": recipe.path,
                    "type": recipe.type,
                    "ingredients": recipe.ingredients,
                    "description": recipe.description,
                }
            }
            return render_template("manager_edit_recipe.html", **context)
    return "please log in"
