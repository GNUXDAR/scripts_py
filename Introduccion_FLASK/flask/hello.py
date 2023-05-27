from flask import Flask, url_for, request, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            return 'Invalid username/password'
    # el siguiente código se ejecuta si el método de solicitud 
    # # era GET o las credenciales no eran válidas

""" otra manera """
# @app.get('/login/')
# def login_get():
#     return show_the_login_form()

# @app.post('/login/')
# def login_post():
#     return do_the_login()

@app.route("/")
def index():
    return "Index Page"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

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
