# Higher Order Functions
# En Python, las funciones se tratan como ciudadanos de primera clase, lo que te permite realizar las siguientes operaciones en las funciones:

# Una función puede tomar una o más funciones como parámetros.
# Una función puede ser devuelta como resultado de otra función.
# Una función puede ser modificada.
# Una función puede ser asignada a una variable.
# En esta sección, cubriremos:

# Manejar funciones como parámetros.
# Devolver funciones como valor de retorno de otras funciones.
# Usar cierres y decoradores en Python.

# Función como parámetro
def sum_numbers(nums):  # funcion normal
    return sum(nums)    # una función triste que abusa de la función de suma incorporada: <


def higher_order_function(f, lst):  # funcion como un parametro
    summation = f(lst)
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15

# FUNCION COMO VALOR DE RETORNO
def square(x):          # una función cuadrada
    return x ** 2

def cube(x):            # una función de cubo
    return x ** 3

def absolute(x):        # una función de valor absoluto
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # una función de orden superior que devuelve una función
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

# python closure
# Python permite que una función anidada acceda al ámbito externo de la función envolvente. 
# Esto se conoce como Cierre. Echemos un vistazo a cómo funcionan los cierres en Python. 
# En Python, el cierre se crea anidando una función dentro de otra función encapsuladora y luego devolviendo la función interna. 
# Vea el ejemplo a continuación.
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20

# Python Decorators
# Un decorador es un patrón de diseño en Python que permite a un usuario agregar una nueva funcionalidad a un objeto existente sin modificar su estructura.
# Los decoradores generalmente se llaman antes de la definición de una función que desea decorar.
# Para crear una función decoradora, necesitamos una función externa con una función contenedora interna.
# Normal function
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## Let us implement the example above with a decorator

'''This decorator function is a higher order function
that takes a function as a parameter'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
