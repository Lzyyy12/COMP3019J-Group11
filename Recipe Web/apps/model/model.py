from apps import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255), nullable=False)
    photo = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name

class Recipe(db.Model):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True)
    path = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Recipe %r>' % self.name