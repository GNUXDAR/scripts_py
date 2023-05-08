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
Nota: antes de una isntalacion activar el entorno: "source env/bin/ activate
pip install Flask-WTF
pip install email-validator
pip install WTForms
pip install flask-login

## Para forzar la instalacion de una extension
pip install --upgrade --force-reinstall Flask-WTF
