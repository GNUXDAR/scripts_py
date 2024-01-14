# Como puedo crear un enlace simbolico en linux para ejecutar un programa de consola en python?
Para crear un enlace simbólico en Linux y ejecutar un programa de consola en Python, puedes seguir los siguientes pasos:  

1. Abre una terminal en tu sistema Linux.
2. Navega hasta el directorio donde se encuentra el programa de Python que deseas ejecutar.
3. Crea el enlace simbólico usando el comando `ln -s` seguido de la ruta al programa de Python y el nombre que deseas asignarle al enlace. Por ejemplo:
   ```
   ln -s /ruta/al/programa.py mi_programa
   ```
   Esto creará un enlace simbólico llamado "mi_programa" que apunta al archivo "/ruta/al/programa.py".
4. Asegúrate de que el programa de Python tenga los permisos adecuados para ejecutarse. Puedes usar el comando `chmod` para establecer los permisos necesarios. Por ejemplo:
   ```
   chmod +x /ruta/al/programa.py
   ```
   Esto otorgará permisos de ejecución al programa.
5. Ahora puedes ejecutar el programa de Python usando el enlace simbólico que has creado. Simplemente escribe el nombre del enlace en la terminal y presiona Enter. Por ejemplo:
   ```
   ./mi_programa
   ```
   Esto ejecutará el programa de Python como si lo hubieras llamado directamente.

Recuerda reemplazar "/ruta/al/programa.py" con la ruta real y el nombre de tu programa de Python. Además, ten en cuenta que es posible que debas tener instalado Python en tu sistema para ejecutar programas de Python.