# Python para Web
Python es un lenguaje de programación de propósito general y se puede usar para muchos lugares. En esta sección, veremos cómo usamos Python para la web. 
Hay muchos framework web de Python. Django y Flask son los más populares. Hoy veremos cómo usar Flask para el desarrollo web.

# Flask
Flask es un framework de desarrollo web escrito en Python. Flask utiliza el motor de plantillas Jinja2. Flask también se puede usar con otras bibliotecas de front modernas como React.

Si aún no instaló el paquete virtualenv, instálelo primero. El entorno virtual permitirá aislar las dependencias del proyecto de las dependencias de la máquina local.

## Estructura de Carpetas
Después de completar todos los pasos, la estructura de archivos de su proyecto debería verse así:
├── Procfile
├── app.py
├── env
│   ├── bin
├── requirements.txt
├── static
│   └── css
│       └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── result.html

## Configurando el directorio de tu proyecto
Siga los siguientes pasos para comenzar con Flask.
Paso 1: instala virtualenv usando el siguiente comando.

    pip install virtualenv

Paso 2:
    $ mkdir flask_project
    $ cd flask_project/
    /flask_project$ virtualenv venv
    flask_project$ source venv/bin/activate
    (env)flask_project$ pip freeze
    (env)flask_project$ pip install Flask
    (env)flask_project$ pip freeze
        blinker==1.6.2
        click==8.1.3
        Flask==2.3.1
        itsdangerous==2.1.2
        Jinja2==3.1.2
        MarkupSafe==2.1.2
        Werkzeug==2.3.1
    (env)flask_project$

Creamos un director de proyecto llamado flask_project. Dentro del proyecto creamos un entorno virtual venv que podría tener cualquier nombre pero prefiero llamarlo venv. Luego activamos el entorno virtual. Usamos "pip freeze" para verificar los paquetes instalados en el directorio del proyecto. El resultado de la congelación de pip estaba vacío porque aún no se había instalado un paquete.

Ahora, creemos el archivo app.py en el directorio del proyecto. El archivo app.py será el archivo principal del proyecto. 