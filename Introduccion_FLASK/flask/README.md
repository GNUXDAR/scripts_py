# Sistema de Gestion de personal

## creando el entorno virtual
python3 -m venv .venv
. .venv/bin/activate

## Install Flask
pip install flask
pip freeze

## Ejecutando el fichero
flask --app hello run       (fichero se llama hello.py)
flask --app hello run --debug
Nota:
Como atajo, si el archivo se llama app.py o wsgi.py, no tiene que usar --app. Consulte Interfaz de línea de comandos para obtener más detalles.


source env/bin/activate
flask run --debug

## Instalando el framework y modulo de conexion
pip install flask
install mysql-client    (pedia instalar "flask-mysqldb" pero daba error)
