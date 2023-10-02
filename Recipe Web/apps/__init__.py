from flask import Flask,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from apps import config

from apps.api.recepies import bp as recepies_bp
# from apps.api.login import bp as login_bp
# from apps.api.register import bp as register_bp

app = Flask(__name__,static_folder='./static')
app.config.from_object(config)
# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'ly_flask'
USERNAME = 'root'
PASSWORD = '123456'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# 注册提供静态文件的蓝图
app.register_blueprint(recepies_bp)
# app.register_blueprint(login_bp)
# app.register_blueprint(register_bp)