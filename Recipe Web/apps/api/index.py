from flask import Flask, request, jsonify, Blueprint, render_template, session
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