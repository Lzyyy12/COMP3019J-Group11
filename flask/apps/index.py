from flask import Flask, render_template, Blueprint

bp=Blueprint("index",__name__,url_prefix="/")

@bp.route("/")
def index():
    return render_template("index.html")