from flask import Flask, url_for, request
from markupsafe import escape


app = Flask(__name__)


@app.route('/login/')
def login():
    return 'The login page'

@app.route("/")
def index():
    return "Index Page"

@app.route('/hello/')
def hello():
    return 'Hello world!'

@app.route('/projects/')
def projects():
    return ' The project page'

@app.route('/about/')
def about():
    return 'The About page'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
