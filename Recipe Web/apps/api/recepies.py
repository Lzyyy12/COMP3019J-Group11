from flask import Flask, request, jsonify, Blueprint, render_template
from apps.model.model import Recipe
from apps import db
import json

bp = Blueprint("recipe", __name__, url_prefix="/api")


# @bp.route('/addrecipe', methods=['POST'])
# def addrecipe():
#     data = request.get_data()
#     json_data = json.loads(data)
#     name = json_data.get('name')
#     imgpath = json_data.get('imgpath')
#     detail = json_data.get('detail')

#     if not name or not imgpath or not detail:
#         return 'input error'

#     newobj = User(username=name, email=imgpath, password=detail)
#     db.session.add(newobj)
#     db.session.commit()
#     users = User.query.all()
#     return render_template('addrecipe.html', users=users)


@bp.route("/getrecipe", methods=["GET"])
def getALlRecipe():
    recipe_obj = Recipe.query

    for i in recipe_obj:
        
        i += i

    cplist = [
        {"name": "Dish A", "path": "#"},
        {"name": "Dish B", "path": "#"},
    ]

    context = {
        "cplist": cplist
    }
    context["cplist"]
    return render_template("recipe.html", **context)
