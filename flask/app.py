from flask import Flask, render_template, Blueprint
import config

from apps.index import bp as index_bp
from apps.recipe import bp as recipe_bp
from apps.about import bp as about_bp

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(index_bp)
app.register_blueprint(recipe_bp)
app.register_blueprint(about_bp)


if __name__ == '__main__':
    app.run(debug=True)
