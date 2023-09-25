from flask import Flask, render_template, Blueprint

bp=Blueprint("about",__name__,url_prefix="/about")

@bp.route('/')
def about():
    context={
        "recipe_name":"Apple Pie"
    }
    return render_template("about.html",**context)