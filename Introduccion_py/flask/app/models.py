from flask import url_for
from slugify import slugify
from sqlalchemy.exc import IntegrityError

from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'blog_user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    title_slug = db.Column(db.String(256), unique=True, nullable=False)
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post {self.title}>'

