## Tutorial de FLASK
## creando el entorno virtual
mkdir flask_todolist

cd flask_todolist

python3 -m venv .venv 

. .venv/bin/activate ó source .venv/bin/activate

## Instalando el framework y modulo de conexion
pip install flask

## Ejecutando el proyecto
flask --app flaskr init-db

flask --app flaskr run --debug

ir a http://127.0.0.1:5000


## Inicializar el archivo de base de datos
Si todavía está ejecutando el servidor desde la página anterior, puede detener el servidor o ejecutar este comando en una nueva terminal. Si usa una terminal nueva, recuerde cambiar al directorio de su proyecto y activar el env como se describe en Instalación.

flask --app flaskr init-db
Initialized the database.

## Comando para ejecutar las pruebas
pip install pytest coverage

pytest ó coverage run -m pytest
