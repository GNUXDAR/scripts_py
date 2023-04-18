print("""
Este directorio fue creado desde el fihero 'modulos.py' 

import os
directory = 'directory_gnuxdar_created_with_os_module'
# Creando un directorio
if os.path.exists(directory):
    print('Existe')
else:
    os.mkdir('directory_gnuxdar_created_with_os_module')
# Cambiar el directorio actual
os.chdir('directory_gnuxdar_created_with_os_module')
# Obtener el directorio de trabajo actual
# "getcwd" es una abreviatura de "get current working directory".
print('el directorio actual es ', os.getcwd())
# Eliminar el directorio
# os.rmdir('directory_gnuxdar_created_with_os_module')   # da error porque esta en otro espacio de trabajo ;)
    """)
