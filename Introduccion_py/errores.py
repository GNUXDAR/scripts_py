# Cuando escribimos código es común que cometamos errores tipográficos u otros errores comunes. 
# Si nuestro código no se ejecuta, el intérprete de Python mostrará un mensaje que contiene comentarios con información 
# sobre dónde ocurre el problema y el tipo de error. A veces, también nos dará sugerencias sobre una posible solución. 
# Comprender los diferentes tipos de errores en los lenguajes de programación nos ayudará a depurar nuestro código rápidamente 
# y también nos hará mejores en lo que hacemos.

# Veamos los tipos de error más comunes uno por uno. Primero, abramos nuestro shell interactivo de Python. 
# Vaya a la terminal de su computadora y escriba 'python'. Se abrirá el shell interactivo de python.

# SyntaxError
print 'hello world'

#   File "<stdin>", line 1
# print 'hello world'
# ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?

# Como puede ver, cometimos un error de sintaxis porque olvidamos encerrar la cadena entre paréntesis y Python ya sugiere la solución. Arreglemoslo.

print('Hello Worl')
# El error fue un SyntaxError. Después de la corrección, nuestro código se ejecutó sin problemas. Veamos más tipos de errores.

# NameError
print(age)
# File "<stdin>", line 1, in <module >
# NameError: name 'age' is not defined

# IndexError
numbers = [1, 2, 3, 4, 5]
numbers[5]
# IndexError: list index out of range
    # En el ejemplo anterior, Python generó un IndexError porque la lista solo tiene índices del 0 al 4, por lo que estaba fuera de rango.

# ModuleNotFoundError
import maths
# ModuleNotFoundError: No module named 'maths'
    # En el ejemplo anterior, agregué una s adicional a las matemáticas deliberadamente y se generó ModuleNotFoundError. 
    # Vamos a solucionarlo eliminando las s adicionales de las matemáticas.

# AttributeError
import math
math.PI   #es math.pi
# AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?

# KeyError
users = {'name':'Arturo', 'age':33, 'country':'Ecuador'}
users['county'] #es users['country']
# KeyError: 'county'

# TypeError
4 + '3'
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# ImportError
# Example 1: TypeError
from math import power
# ImportError: cannot import name 'power' from 'math' (unknown location)
# es: from math import pow
# pow(2, 3)

# ValueError
int('12a')
# ValueError: invalid literal for int() with base 10: '12a'

# ZeroDivisionError
1/0
# ZeroDivisionError: division by zero

# Hemos cubierto algunos de los tipos de error de python, si desea obtener más información al respecto, 
# consulte la documentación de python sobre los tipos de error de python. 
# Si es bueno para leer los tipos de errores, podrá corregirlos rápidamente y también se convertirá en un mejor programador. 

