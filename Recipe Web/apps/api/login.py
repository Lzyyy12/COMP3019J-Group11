from flask import Flask, request, jsonify, Blueprint, render_template, session, url_for, redirect
import json
from apps.model.model import User
from apps import db

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
            return redirect('./main')
        else:
            context["msg"] = 'User name not exist or wrong password，please input name and password again to login!'
            return render_template('login.html', **context)
    return render_template('login.html', **context)


@bp.route("/register", methods=["GET", "POST"])
def register():
    context = {
        "msg": 'please input name and password to register!'
    }
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 检查用户名是否已经存在
        existing_user = User.query.filter_by(name=username).first()
        if existing_user:
            context["msg"] = "Username already exists. Please choose a different username."
            return render_template('register.html', **context)
        # 创建一个新用户对象
        new_user = User(name=username, password=password)
        # 将新用户添加到数据库并提交更改
        db.session.add(new_user)
        db.session.commit()

        # 重定向到登录页面
        return redirect('./login')
    return render_template('register.html', **context)


@bp.route('/logout')
def logout():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        session.pop('logged_in')
        return redirect('/')