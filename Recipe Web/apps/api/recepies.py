from flask import Flask,request,jsonify, Blueprint,render_template

bp = Blueprint("recipes",__name__,url_prefix="/")

@bp.route("/",methods=["GET"])
def recipes():
    recipe_list=[
        {"name":"Apple Pie","path":"#"},
        {"name":"Pineapple Pizza","path":"#"},
    ]
    
    context={
        "recipe_list":recipe_list
    }
    return render_template("index.html",**context)