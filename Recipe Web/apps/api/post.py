from flask import Flask, request, jsonify, Blueprint, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from apps.model.model import User
from apps import db

bp = Blueprint("post", __name__, url_prefix="/api")

# Login route
@bp.route("/post", methods=["GET", "POST"])
def post():
        return redirect('/')