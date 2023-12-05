from flask import Flask, request, jsonify, Blueprint, render_template, session
from apps.model.model import Recipe
from apps import db
import apps.api
bp = Blueprint("index", __name__, url_prefix="/")

@bp.route("/", methods=["GET"])
@bp.route("/index", methods=["GET"])
def index():
    context = {
        "islogin": False
    }
    # Check login status
    if session.get('logged_in'):
        context["islogin"] = True
        context["usermsg"] = session.get('username')
    return render_template("index.html", **context)

@bp.route("/search", methods=["GET"])
def search():
    keyword = request.args.get("keyword")
    cplist = []
    # Get the list of recipes from database
    recipe_objs = Recipe.query.filter(Recipe.name.like(keyword)).all()
    for recipe in recipe_objs:
        recipedata = {}
        recipedata['name'] = recipe.name
        recipedata['path'] = recipe.path
        cplist.append(recipedata)
   
    context = {
        "cplist": cplist
        }
    
    return render_template("recipe.html", **context)
