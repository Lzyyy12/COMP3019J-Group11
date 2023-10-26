from flask import Flask, request, jsonify, Blueprint, render_template, session, url_for, redirect
import json
from apps.model.model import User
from apps import db

bp = Blueprint("login", __name__, url_prefix="/api")


@bp.route("/login", methods=["GET", "POST"])
def login():
    context = {
        "msg": 'Please input name and password to login!'
    }
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_obj = User.query.filter_by(name=username).first()

        if username == user_obj.name and password == user_obj.password:
            session["username"] = username
            session['logged_in'] = user_obj.id
            return redirect('./main')
        else:
            context["msg"] = 'User name not exist or wrong password，please input name and password again to login!'
            return render_template('login.html', **context)
    return render_template('login.html', **context)


@bp.route("/register", methods=["GET", "POST"])
def register():
    context = {
        "msg": 'Please input name and password to register!'
    }
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists.
        existing_user = User.query.filter_by(name=username).first()
        if existing_user:
            context["msg"] = "Username already exists. Please choose a different username."
            return render_template('register.html', **context)
        # Create a new user and store to database.
        new_user = User(name=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        # Redirect to login page.
        return redirect('./login')
    return render_template('register.html', **context)


@bp.route('/logout')
def logout():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        session.pop('logged_in')
        return redirect('/')