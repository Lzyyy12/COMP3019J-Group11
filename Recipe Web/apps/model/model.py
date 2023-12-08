from apps import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=False)
    type = db.Column(db.Integer, autoincrement=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    path = db.Column(db.String(255), nullable=True)
    type = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return '<Recipe %r>' % self.name
    
class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.String(255), nullable=True)
    
    def __repr__(self):
        return '<Ingredient %r>' % self.name