# CONFIGURACION DE ENTORNOS VIRTUALES
Para empezar con el proyecto, sería mejor tener un entorno virtual. El entorno virtual puede ayudarnos a crear un entorno aislado o separado. Esto nos ayudará a evitar conflictos en las dependencias entre proyectos. Si escribe {pip freeze} en su terminal, verá todos los paquetes instalados en su computadora. Si usamos virtualenv, accederemos solo a los paquetes que son específicos para ese proyecto. Abre tu terminal e instala virtualenv

{{pip install virtualenv}}

dentro de la carpéta crear una carpeta flask_project
Después de instalar el paquete virtualenv, vaya a la carpeta de su proyecto y cree un entorno virtual escribiendo:

### Para Mac/Linux
{{virtualenv venv}}

## Para windows
{{python -m venv venv}}

Prefiero llamar al nuevo proyecto venv, pero siéntete libre de nombrarlo de otra manera. Verifiquemos si el venv se creó usando el comando ls (o dir para el símbolo del sistema de Windows).

Activemos el entorno virtual escribiendo el siguiente comando en nuestra carpeta de proyecto.

### Para Mac/Linux
{{source venv/bin/activate}}

## Para windows power Shell
{{venv\Scripts\activate}}

## Para windows git bash
{{venv\Scripts\. activate}}

Después de escribir el comando de activación, el directorio de su proyecto comenzará con venv.
Ahora, revisemos los paquetes disponibles en este proyecto escribiendo pip freeze. No verá ningún paquete.

Vamos a hacer un pequeño proyecto con Flask, así que instalemos el paquete de Flask para este proyecto.
{{pip install Flask}}

Ahora, escribamos pip freeze para ver una lista de paquetes instalados en el proyecto:
{{pip freeze}}

Cuando termine, debe desactivar el proyecto activo usando deactivate.
{{deactive}}

Los módulos necesarios para trabajar con Flask están instalados. Ahora, el directorio de tu proyecto está listo para un proyecto de Flask. Debes incluir el venv en tu archivo .gitignore para no subirlo a GitHub.