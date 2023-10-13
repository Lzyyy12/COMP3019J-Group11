from flask import Flask, request, jsonify, Blueprint, render_template, session, url_for, redirect
import json
from apps.model.model import User

bp = Blueprint("login", __name__, url_prefix="/api")


@bp.route("/login", methods=["GET", "POST"])
def login():
    context = {
        "msg": 'please input name and password to login!'
    }
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user_obj = User.query.filter_by(name=username).first()

        if username == user_obj.name and password == user_obj.password:
            session["username"] = username
            session['logged_in'] = user_obj.id
            return redirect('/')
        else:
            context["msg"] = 'User name not exist or wrong password，please input name and password again to login!'
            return render_template('login.html', **context)
    return render_template('login.html', **context)


@bp.route("/register", methods=["POST"])
def register():
    data = request.get_data()
    json_data = json.loads(data)
    if True:
        return 'success'
    else:
        return 'fail'


@bp.route('/logout')
def logout():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        session.pop('logged_in')
        return redirect('/')