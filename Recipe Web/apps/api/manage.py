import uuid
from flask import Flask, app, request, jsonify, Blueprint, render_template, session, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, validators
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from apps.model.model import User, Recipe
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