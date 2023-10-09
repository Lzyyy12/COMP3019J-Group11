from flask import Flask, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from apps import config

app = Flask(__name__, static_folder='./static')
app.config.from_object(config)
app.secret_key = '1qaz2wsx'  # 设置密钥

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flaskdemo'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# db.create_all()

#from apps.api.index import bp as index_bp
from apps.api.login import bp as login_bp
#from apps.api.user import bp as user_bp
#from apps.api.recipe import bp as recipe_bp

#app.register_blueprint(index_bp)
app.register_blueprint(login_bp)
#app.register_blueprint(user_bp)
#app.register_blueprint(recipe_bp)