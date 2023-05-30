# Tutorial Flask 
[tutorial](https://flask.palletsprojects.com/)

## creando el entorno virtual
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