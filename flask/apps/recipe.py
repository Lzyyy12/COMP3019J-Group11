from flask import Flask, render_template, Blueprint

bp=Blueprint("recipe",__name__,url_prefix="/recipe")

recipes=[
    {"id":1,"name":"Apple Pie"},
    {"id":2,"name":"Blueberry Pie"},
    {"id":3,"name":"Pineapple Pie"},
    {"id":4,"name":"Pumpkin Pie"},
]

@bp.route("/<int:recipe_id>")

def recipe_list(recipe_id):
    for recipe in recipes:
        if recipe_id==recipe["id"]:
            return recipe
    return "Recipe with id {} not find.".format(recipe_id)
