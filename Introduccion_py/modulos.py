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


# import math
# help(math) # mostrar la descripcion de la libreria
# print(math.cos(math.pi))  #coseno de pi -1.0


# importando un modulo mio (mymodule.py)
import mymodule
print(mymodule.generate_full_name('Arturo', 'Cabrera'))  # Arturo Cabrera

# importando una funcion de un modulo
# Podemos tener muchas funciones en un archivo y podemos importar todas las funciones de manera diferente.

from mymodule import generate_full_name, sum_two_nums, person
person = person('Arturo', 'Cabrera', 33, 'developer')
print(generate_full_name('Arturo','Cabrera'))   # Arturo Cabrera
print(sum_two_nums(1,9))    # 10
print(person['firstname'])  # Arturo

# Importación de funciones desde un módulo y cambio de nombre
# Durante la importación podemos cambiar el nombre del módulo, renombrar.
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p
p = p('Arturo', 'Cabrera', 33, 'developer')
print(fullname('Alexander', 'Cabrera'))  # Alexander Cabrera
print(total(10, 5)) # 15
print(p)    # {'firstname': 'Arturo', 'lastname': 'Cabrera', 'age': 33, 'rol': 'developer'}
print(p['firstname'])   # Arturo

# IMPORTAR MODULOS INTEGRADOS
# Al igual que otros lenguajes de programación, también podemos importar módulos importando el archivo/función usando la palabra clave import. 
# Importemos el módulo común que usaremos la mayor parte del tiempo. 
# Algunos de los módulos incorporados comunes: math, datetime, os,sys, random, statistics, collections, json,re

# OS MODULE
# Usando el módulo python os es posible realizar automáticamente muchas tareas del sistema operativo. 
# El módulo del sistema operativo en Python proporciona funciones para crear, 
# cambiar el directorio de trabajo actual y eliminar un directorio(carpeta), recuperar su contenido, cambiar e identificar el directorio actual.
# import the module
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

# SYS MODULE
# El módulo sys proporciona funciones y variables que se utilizan para manipular diferentes partes del entorno de tiempo de ejecución de Python. 
# La función sys.argv devuelve una lista de argumentos de la línea de comandos pasados ​​a un script de Python. 
# El elemento en el índice 0 de esta lista siempre es el nombre del script, en el índice 1 está el argumento pasado desde la línea de comando.
# para ejecutar, desde el prompt $ python3 test.py Arturo Python30
import sys
print('Welcome {}. Enjoy  {} challenge!'.format(sys.argv[1], sys.argv[2]))

# algunos comandos de sistemas utiles
# para salir del siste
# sys.exit()
# Para conocer la variable entera más grande se necesita
print(sys.maxsize)
# Para conocer la ruta del entorno
print(sys.path)
# Para saber la versión de python que estás usando
print(sys.version)

# MODULO DE ESTADISTICAS 
# El módulo de estadísticas proporciona funciones para estadísticas matemáticas de datos numéricos. 
# Las funciones estadísticas populares que se definen en este módulo: mean, median, mode, stdev etc.
from statistics import * # importando todos los modulos estadisticos
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # 21.09090909090909 media
print(median(ages))     # 23    mediana
print(mode(ages))       # 20    moda
print(stdev(ages))      # 6.106628291529549  desviacion estandar

# MÓDULO MATEMÁTICOS
# Módulo que contiene muchas operaciones matemáticas y constantes.
import math
print(math.pi)           # 3.141592653589793 pi constant
print(math.sqrt(2))      # 1.4142135623730951 raiz cuadrada
print(math.pow(2, 3))    # 8.0 funciona exponencial
print(math.floor(9.81))  # 9 redondeando al mínimo
print(math.ceil(9.81))   # 10 redondeando al maximo
print(math.log10(100))   # 2.0  logaritmo con 10 como base

# Si queremos importar solo una función específica del módulo, la importamos de la siguiente manera
from math import pi
print(pi)

# También es posible importar múltiples funciones a la vez
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(log10(100))         # 2

# Pero si queremos importar todas las funciones en el módulo matemático, podemos usar * .
from math import *
print(pi)                  # 3.141592653589793 pi constant
print(sqrt(2))             # 1.4142135623730951 raiz cuadrada
print(pow(2, 3))           # 8.0 funciona exponencial
print(floor(9.81))         # 9 redondeando al mínimo
print(ceil(9.81))          # 10 redondeando al maximo
print(math.log10(100))     # 2.0  logaritmo con 10 como base

# Cuando importamos también podemos renombrar el nombre de la función.
from math import pi as  PI
print(PI) # 3.141592653589793

# MODULO DE CADENAS
# Un módulo de cadena es un módulo útil para muchos propósitos. El siguiente ejemplo muestra algunos usos del módulo de cadena.
import string
help(string)
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# DATA
# __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
#            ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#            ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
#            ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#            digits = '0123456789'
#            hexdigits = '0123456789abcdefABCDEF'
#            octdigits = '01234567'
#            printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
#            punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#            whitespace = ' \t\n\r\x0b\x0c'

# MODULO RANDOM 
# A estas alturas ya está familiarizado con la importación de módulos. 
# Hagamos una importación más para familiarizarnos con ella. 
# Importemos un módulo aleatorio que nos da un número aleatorio entre 0 y 0.9999.... 
# El módulo aleatorio tiene muchas funciones, pero en esta sección solo usaremos random y randint.
from random import random, randint
help(random)
print(random())   # no necesita ningún argumento; devuelve un valor entre 0 y 0.9999
print(randint(5, 20)) # devuelve un número entero aleatorio entre [5, 20] inclusive