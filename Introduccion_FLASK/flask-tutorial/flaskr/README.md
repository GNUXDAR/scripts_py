# Tutorial Flask 
[tutorial](https://flask.palletsprojects.com/)
[Flask](https://flask.palletsprojects.com/en/2.3.x/tutorial/)

## creando el entorno virtual
mkdir flaskr
cd flaskr
python3 -m venv .venv
. .venv/bin/activate

## Install Flask
pip install flask
pip freeze

## Ejecutando el fichero
flask --app flaskr run --debug
Nota:
ejecutar: (en este directorio:  ~/scripts_py/Introduccion_FLASK/flask-tutorial)


source env/bin/activate
flask run --debug

## Instalando el framework y modulo de conexion
pip install flask
install mysql-client    (pedia instalar "flask-mysqldb" pero daba error)


## ASi debera quedar el proyecto
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── .venv/
├── pyproject.toml
└── MANIFEST.in

## Inicializar el archivo de base de datos
Si todavía está ejecutando el servidor desde la página anterior, puede detener el servidor o ejecutar este comando en una nueva terminal. Si usa una terminal nueva, recuerde cambiar al directorio de su proyecto y activar el env como se describe en Instalación.

$ flask --app flaskr init-db
Initialized the database.