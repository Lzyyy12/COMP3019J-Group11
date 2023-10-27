from flask import Flask, request, jsonify, Blueprint, render_template
from apps.model.model import Recipe
from apps import db
import json

bp = Blueprint("recipe", __name__, url_prefix="/api")

@bp.route("/get_recipe", methods=["GET"])
def get_recipe():
    type = request.args.get("type")
    cplist = []

    recipe_objs = Recipe.query.all()
    for recipe in recipe_objs:
        if type == recipe.type or type == 'all':
            recipedata = {}
            recipedata['name'] = recipe.name
            recipedata['path'] = recipe.path
            cplist.append(recipedata)
   
    context = {
        "cplist": cplist
        }
    
    return render_template("recipe.html", **context)
