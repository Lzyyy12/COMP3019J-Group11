from flask import Flask, request, jsonify, Blueprint, render_template, session
from apps.model.model import Recipe
from apps import db
import apps.api
bp = Blueprint("admin", __name__, url_prefix="/")

@bp.route("/admin", methods=["GET"])
def admin():
    context = {
        "islogin": False
    }
    # Check login status
    if session.get('logged_in'):
        context["islogin"] = True
        context["usermsg"] = session.get('username')
    return render_template("admin.html", **context)

