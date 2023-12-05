import uuid
from flask import Flask, app, request, jsonify, Blueprint, render_template, session, flash, url_for, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField, validators
from flask_wtf.file import FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from apps.model.model import Recipe
from apps import db
import os
import json

bp = Blueprint("recipe", __name__, url_prefix="/api")

@bp.route("/get_recipe", methods=["GET"])
def get_recipe():
    type = request.args.get("type")
    cplist = []
    # Get the list of recipes from database
    recipe_objs = Recipe.query.all()
    for recipe in recipe_objs:
        # Identify type of recipe
        if type == recipe.type or type == 'all':
            recipedata = {}
            recipedata['name'] = recipe.name
            recipedata['path'] = recipe.path
            cplist.append(recipedata)
   
    context = {
        "cplist": cplist
        }
    
    return render_template("recipe.html", **context)

class RecipeForm(FlaskForm):
    name = StringField('name', validators=[validators.DataRequired()])
    image = FileField('image', validators=[FileRequired()])
    recipe_type = SelectField('type', choices=[('eastern', 'Eastern'), ('western', 'Western')],
                              validators=[validators.DataRequired()])

@bp.route("/edit_recipe", methods=["GET", "POST"])
def edit_recipe():
    if session.get('logged_in'):
        if request.method == 'POST':
            form = RecipeForm()

            if form.validate_on_submit():
                name = form.name.data
                image = form.image.data
                recipe_type = form.recipe_type.data

                # 保存文件到服务器

                filename = secure_filename(str(uuid.uuid4()) + '_' + image.filename)
                file_path = os.path.join(app.config['UPLOAD_IMAGE_FOLDER'], filename)
                image.save(file_path)

                # 将文件路径存储到数据库
                new_recipe = Recipe(name=name, path=file_path, type=recipe_type)
                db.session.add(new_recipe)
                db.session.commit()

                flash('Recipe added successfully!', 'success')
            return redirect('/')  # 跳转
        return render_template('edit_recipe.html')
    return "please log in"
