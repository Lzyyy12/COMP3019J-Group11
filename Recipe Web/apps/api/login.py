from flask import Flask, request, jsonify, Blueprint, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length
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
            # Session是一个字典对象
            session["username"] = username
            session['logged_in'] = user_obj.id
            return redirect('/')
        else:
            context["msg"] = 'Username not exist or wrong password，please input name and password again to login!'
            return render_template('login.html', **context)
    return render_template('login.html', **context)


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    context = {
        "msg": 'Please input name and password to register!'
    }
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        if len(username) < 6 or len(password) < 6:
            flash('Username and password must be at least 6 characters long.', 'error')
        else:
            existing_user = User.query.filter_by(name=username).first()
            if existing_user:
                flash('Username already exists. Please choose a different username.', 'error')
            else:
                new_user = User(name=username, password=password)
                db.session.add(new_user)
                db.session.commit()
                flash('Registration successful. You can now log in.', 'success')
                return redirect(url_for('login.login'))
    return render_template('register.html', form=form, **context)


@bp.route('/logout')
def logout():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        session.pop('logged_in')
        return redirect('/')