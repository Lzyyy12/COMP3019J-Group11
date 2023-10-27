from flask import Flask, request, jsonify, Blueprint, render_template, session, url_for, redirect, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from apps.model.model import User
from apps import db

bp = Blueprint("login", __name__, url_prefix="/api")

# Login Form using Flask-WTF
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

# Login route
@bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    context = {
        "msg": 'Please input name and password to login!'
    }
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        user_obj = User.query.filter_by(name=username).first()
        if user_obj is not None:
            if check_password_hash(user_obj.password, password):
                # If username and password match an existing user, log in the user
                session["username"] = username
                session['logged_in'] = user_obj.id
                return redirect('/')
            # If login fails, show an error message using flash
            flash('Username not exist or wrong password，please input again to login!', 'error')
        else:
            # If login fails, show an error message using flash
            flash('Username not exist or wrong password，please input again to login!', 'error')
    return render_template('login.html', form=form, **context)


# Registration Form using Flask-WTF
class RegistrationForm(FlaskForm):
    # Validation: username and password should be at least 6 charactor long, the confirmpassword mush match the password
    username = StringField('Username', validators=[DataRequired(), Length(min=6)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirmpassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])

@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    context = {
        "msg": 'Please input name and password to register!'
    }
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        confirmpassword = form.confirmpassword.data

        if password != confirmpassword:
            flash('Passwords do not match. Please enter matching passwords.', 'error')
        else:
            hashed_password = generate_password_hash (password)

        existing_user = User.query.filter_by(name=username).first()
        if existing_user:
            # If the username already exists, flash an error message
            flash('Username already exists. Please choose a different username.', 'error')
        else:
            # If all checks pass, create a new user and add it to the database
            new_user = User(name=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login.login'))
    return render_template('register.html', form=form, **context)


@bp.route('/logout')
def logout():
    if not session.get('logged_in'):
        # If the user is not logged in, redirect to the login page
        return redirect(url_for('login'))
    else:
        session.pop('logged_in')
        # If the user is logged in, log them out and redirect to the homepage
        return redirect('/')