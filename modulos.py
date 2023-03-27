# modulos
# cada uno de los archivos .py que generamos en python se denominan modulos, y son considerados contenedores para organizar nuestro codigo

#paquetes
# un paquete es un modulo que sirve para contener otros modulos y paquetes, en la practica es un directorio que contiene un archivo '__init__.py
# dentro de dicho directorio podremos tener almacenados otros modulos o paquetes
# .
# |-- modulo1.py
# |-- paquete
#   |-- __init__.py
#   |-- modulo1.py
#   |-- subpaquete
#       |-- __init__.py
#       |-- modulo1.py
#       |-- modulo2.py


import math
help(math) # mostrar la descripcion de la libreria
print(math.cos(math.pi))  #coseno de pi