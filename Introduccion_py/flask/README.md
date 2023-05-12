## Ejecutar el proyecto Flask
$ source env/bin/activate
$ flask run --debug

## A una URL de podemos añadir secciones variables o parametrizadas
Por defecto, en Flask existen los siguientes conversores:

* string: Es el conversor por defecto. Acepta cualquier cadena que no contenga el carácter ‘/’.
* int: Acepta números enteros positivos.
* float: Acepta números en punto flotante positivos.
* path: Es como string pero acepta cadenas con el carácter ‘/’.
* uuid:  Acepta cadenas con formato UUID.

@app.route("/p/<string:slug>/")

## Extensiones
Nota: antes de una instalacion activar el entorno: "source env/bin/ activate
pip freeze  (mostrar los modulos instalados)
pip install Flask-WTF
pip install email-validator
pip install WTForms
pip install flask-login

pip install flask-sqlalchemy   <!--  ORM -->
pip install psycopg2           <!--  postgresql -->
pip install mysql-connector-python  <!-- mysql -->
pip install python-slugify


## Para forzar la instalacion de una extension
pip install --upgrade --force-reinstall Flask-WTF

## Crear la base de datos
desde el REPL ejecutar

from app import db
db.create_all()