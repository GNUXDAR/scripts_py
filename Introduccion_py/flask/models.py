from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from slugify import slugify
from sqlalchemy.exc import IntegrityError

class User(db.Model, UserMixin):

    __tablename__ = 'blog_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80),  nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    id_admin = db.Column(db.Boolean, default=False)
    
    # def __init__(self, id, name, email, password, is_admin=False):
    #     self.id = id
    #     self.name = name
    #     self.email = email
    #     self.password = generate_password_hash(password)
    #     self.is_admin = is_admin

    def set_password(self, password):
        """Envio de contraseñas"""
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """verificar contraseña de usuario"""
        return check_password_hash(self.password, password)

    def __repr__(self):
        """retornar email"""
        return f'<User {self.email}>'
    
    def save(self):
        """ salvar la session """
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        """ obtener el id """
        return User.query.get(id)
    
    @staticmethod
    def get_by_email(email):
        """ obtener el email """
        return User.query.filter_by(email=email).first()
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('blog_user.id', ondelete='CASCADE'), nullable=False)
    title = db.Column(db.String(256), nullable=False)
    title_slug = db.Column(db.String(256), unique=True, nullable=False)
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Post {self.title}>'

    def save(self):
        if not self.id:
            db.session.add(self)
        if not self.title_slug:
            self.title_slug = slugify(self.title)
        saved = False
        count = 0
        while not saved:
            try:
                db.session.commit()
                saved = True
            except IntegrityError:
                count += 1
                self.title_slug = f'{slugify(self.title)}-{count}'

    def public_url(self):
        return url_for('show_post', slug=self.title_slug)

    @staticmethod
    def get_by_slug(slug):
        return Post.query.filter_by(title_slug=slug).first()

    @staticmethod
    def get_all():
        return Post.query.all()
