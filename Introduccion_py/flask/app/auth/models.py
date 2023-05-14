from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db


class User(db.Model, UserMixin):

    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.email}>'

    ...
