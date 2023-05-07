# Toda aplicación Flask es una instancia WSGI de la clase Flask.
from flask import Flask, render_template, url_for, request, redirect
from forms import SignupForm, PostForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

posts = []

@app.route('/')
def index():
    """ ruta del home """
    page = request.args.get('page', 1)
    list = request.args.get('list', 20)

    return render_template('index.html', title='home', num_post=len(posts), posts=posts)


@app.route('/p/<string:slug>/')
def show_post(slug):
    """ mostrar los post con slug """
    return render_template('post_view.html', slug_title=slug)


# crear - editar
@app.route('/admin/post/', methods=['GET', 'POST'])
@app.route('/admin/post/<int:post_id>/')
def post_form(post_id=None):
    """ crear y editar """
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        title_slug = form.title_slug.data
        content = form.content.data

        post = {'title': title, 'title_slug': title_slug, 'content': content}
        posts.append(post)  #guardando en un dicionario post_form.html

        return redirect(url_for('index'))
    return render_template('admin/post_form.html', form=form)

# registro
@app.route('/signup/', methods=['GET', 'POST'])
def show_signup_form():
    """ registrar usuario """
    form = SignupForm()
    if form.validate_on_submit():
        name = form.name.date
        email = form.email.data
        password = form.password.data

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return redirect(url_for('index'))

    return render_template('signup_form.html', form=form)
