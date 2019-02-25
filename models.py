from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Post(db.Model):                               # DB model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    sub_title = db.Column(db.String(128))
    author = db.Column(db.String(64), index=True)
    date_post = db.Column(db.DateTime)
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Author: {self.author}, post title: {self.title}>'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String, index=True)
    pwd_hash = db.Column(db.String)

    def set_password(self, password):
        self.pwd_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwd_hash, password)
