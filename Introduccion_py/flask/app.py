# Toda aplicación Flask es una instancia WSGI de la clase Flask.
from flask import Flask, render_template, url_for, request, redirect
from forms import SignupForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

posts = []

@app.route('/')
def index():
    """ ruta del home """
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)

    return render_template('index.html', title='home', num_post=len(posts))

@app.route('/p/<string:slug>/')
def show_post(slug):
    """ mostrar los post con slug """
    return render_template('post_view.html', slug_title=slug)


# crear - editar
@app.route('/admin/post/')
@app.route('/admin/post/<int:post_id>/')
def post_form(post_id=None):
    """ crear y editar """
    # return f'post_form {post_id}'
    return render_template('admin/post_form.html', post_id=post_id)

# registro
@app.route('/signup/', methods=['GET', 'POST'])
def show_signup_form():
    """ registrar usuario """
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.date
        email = form.email.data
        password = form.password.data
    # if request.method == 'POST':
    #     name = request.form['name']
    #     email = request.form['email']
    #     password = request.form['password']

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))

    return render_template('signup_form.html', form=form)