# Toda aplicación Flask es una instancia WSGI de la clase Flask.
from flask import Flask, render_template, url_for, request, redirect
from flask_login import LoginManager, logout_user, current_user, login_user, login_required
from flask_sqlalchemy import SQLAlchemy

from forms import SignupForm, PostForm, LoginForm
from models import users, get_user
from models import User, Post
# import config

import mysql.connector

app = Flask(__name__)
# app.config['SECRET_KEY'] = config.HEX_SEC_KEY
# app.config['MYSQL_HOST'] = config.MYSQL_HOST
# app.config['MYSQL_USER'] = config.MYSQL_USER
# app.config['MYSQL_PASSWORD'] = config.MYSQL_PASSWORD
# app.config['MYSQL_DB'] = config.MYSQL_DB

# cnx = mysql.connector.connect(
#     user='root', password='#Pass1234', host='localhost', database='py_flask')
# cursor = cnx.cursor()
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:#Pass1234@localhost/py_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

login_manager = LoginManager(app)
login_manager.login_view = 'login'
# objeto SQLAlchemy
db = SQLAlchemy(app)
from models import User

posts = []

@app.route('/')
def index():
    """ ruta del home """
    posts = Post.get_all()

    return render_template('index.html', title='home', posts=posts)


@app.route('/p/<string:slug>/')
def show_post(slug):
    """ mostrar los post con slug """
    post = Post.get_by_slug(slug)
    if post is None:
        abort(404)
    return render_template('post_view.html', post=post)


# crear - editar
@app.route('/admin/post/', methods=['GET', 'POST'], defaults={'post_id': None})
@app.route('/admin/post/<int:post_id>/', methods=['GET', 'POST'])
@login_required # proteger el acceso a la vista solo  a los usuarios autenticados
def post_form(post_id):
    """ crear y editar """
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        post = Post(user_id=current_user.id, title=title, content=content)
        post.save()

        return redirect(url_for('index'))
    return render_template('admin/post_form.html', form=form)

# registro
@app.route('/signup/', methods=['GET', 'POST'])
def show_signup_form():
    """ registrar usuario """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = SignupForm()
    error = None

    if form.validate_on_submit():
        name = form.name.date
        email = form.email.data
        password = form.password.data
        # validamos user con el mismo email
        user = User.get_by_email(email)
        if user is not None:
            error = f'El email {email} ya se encuentra utilizado'
        else:
            # creamos el user y lo guardamos
            user = User(name=name, email=email)
            user.set_password(password)
            user.save()

            # dejamos al user logueado
            login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('signup_form.html', form=form, error=error)

# vista del login
@app.route('/login/', methods=['GET', 'POST'])
def login():
    """ login de la app """
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('index')
            return redirect(next_page)
    return render_template('login_form.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    """cargar usuarios"""
    return User.get_by_id(int(user_id))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))