from flask import Flask, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from apps import config
import os

app = Flask(__name__)
app.config['STATIC_FOLDER'] = os.getenv('STATIC_FOLDER')
app.config['UPLOAD_IMAGE_FOLDER'] = os.getenv('UPLOAD_IMAGE_FOLDER')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


from apps.api.index import bp as index_bp
from apps.api.login import bp as login_bp
from apps.api.recipe import bp as recipe_bp

from apps.api.admin import bp as admin_bp
from apps.api.manage import bp as manage_bp

app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
app.register_blueprint(recipe_bp)

app.register_blueprint(admin_bp)
app.register_blueprint(manage_bp)