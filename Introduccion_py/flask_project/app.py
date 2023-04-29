# vamos a importar flask
from flask import Flask
import os  # importar el módulo del sistema operativo

app = Flask(__name__)


@app.route('/')  # este decorador crea la ruta home
def home():
    return '<h1>Welcome</h1>'


@app.route('/about')
def about():
    return '<h1>About us</h1>'


if __name__ == '__main__':
    # para el despliegue usamos el entorno 
    # para que funcione tanto para la producción como para el desarrollo
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
