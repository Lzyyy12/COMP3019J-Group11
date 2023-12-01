from flask import Flask, request, jsonify, Blueprint, render_template, session
from apps.model.model import Recipe
from apps import db
import json

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

@bp.route("/edit_recipe", methods=["GET", "POST"])
def edit_recipe():
    if session.get('logged_in'):
        if request.method == 'POST':
            return 0
        return render_template('edit_recipe.html')
    return "please log in"
