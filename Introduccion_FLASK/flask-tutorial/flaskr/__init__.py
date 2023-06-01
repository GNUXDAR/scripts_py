import os

from flask import Flask


def create_app(test_config=None):
    # crear y configurar la aplicación
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    from . import db
    db.init_app(app)

    if test_config is None:
        # cargar la configuración de la instancia, si existe, cuando no se está realizando pruebas
        app.config.from_pyfile('config.py', silent=True)
    else:
        # cargar la configuración de prueba si se pasa
        app.config.from_mapping(test_config)

    # asegurarse de que la carpeta de instancia exista
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # una página simple que dice hola
    @app.route('/hello/')
    def hello():
        return 'Hello, World! Arturo'
    
    # blueprint auth
    from . import auth
    app.register_blueprint(auth.bp)

    # blueprint blog
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app
