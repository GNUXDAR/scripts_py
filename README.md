  <a class="header-badge" target="_blank" href="https://arturocabrera.com/etiqueta/python">
  <img src="https://github.com/GNUXDAR/scripts_py/blob/main/img/py_img.png">
  </a>

[Blog Web](https://arturocabrera.com/blog) | [Recursos Web](Docs/README.md) | [Recursos PDF](Docs/PDF/pdfs.md)

Jupyter Notebook, una aplicación web de código abierto, 
le permite crear y compartir un código interactivo, 
visualizaciones y otros recursos en la web.

pip is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.   $ pip list

# Paso 1: Configurar Python
    sudo apt update
    sudo apt install python3-pip python3-dev

# Paso 2: Crear un entorno virtual de Python para Jupyter
    sudo -H pip3 install --upgrade pip
    sudo -H pip3 install virtualenv

    mkdir ~/scripts_py
    cd ~/scripts_py

    virtualenv scripts_py_env

    source scripts_py_env/bin/activate

# Paso 3: Instalar Jupyter
    pip install jupyter

# Paso 4: Ejecutar Jupyter Notebook
    jupyter notebook

# Post instalacion
    source scripts_py_env/bin/activate
    jupyter notebook