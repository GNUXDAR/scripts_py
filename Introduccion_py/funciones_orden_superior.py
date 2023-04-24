# Higher Order Functions
# En Python, las funciones se tratan como ciudadanos de primera clase, lo que te permite realizar las siguientes operaciones en las funciones:

# Una función puede tomar una o más funciones como parámetros.
# Una función puede ser devuelta como resultado de otra función.
# Una función puede ser modificada.
# Una función puede ser asignada a una variable.
# En esta sección, cubriremos:

# Manejar funciones como parámetros.
# Devolver funciones como valor de retorno de otras funciones.
# Usar closure y decoradores en Python.

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
# Esto se conoce como Cierre ó Closure. Echemos un vistazo a cómo funcionan los cierres en Python.
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

# Implementemos el ejemplo anterior con un decorador.
"""Esta función decoradora es una función de orden superior que toma una función como parámetro"""
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

# Aplicando múltiples decoradores a una sola función
'''These decorator functions are higher order functions
that take functions as parameters'''

# First Decorator
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Second decorator
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # order with decorators is important in this case - .upper() function does not work with lists
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON

# Aceptando parámetros en funciones de decorador
# La mayoría de las veces necesitamos que nuestras funciones tomen parámetros, por lo que es posible que debamos definir un decorador que acepte parámetros.
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print('I live in {}'.format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print('I am {} {}. I love to teach.'.format(
        first_name, last_name, country))

print_full_name('Arturo', 'Cabrera','Equator')

# FUNCIONES INTEGRADAS DE ORDEN SUPERIOR
# Algunas de las funciones integradas de orden superior que cubrimos en esta parte son map(), filter y reduce. 
# La función lambda se puede pasar como un parámetro y el mejor caso de uso de las funciones lambda es en funciones como map, filter y reduce.

# Python - Map Function
# La función map() es una función integrada que toma una función y es iterable como parámetros.
# syntax
map(function, iterable)

# ejemplo 1:
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# Vamos a aplicarlo con una función lambda
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]

# Ejemplo2 
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]

# Ejemplo 3
names = ['Arturo', 'Cabrera', 'Dev', 'Blogger']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ARTURO', 'CABRERA', 'DEV', 'BLOGGER']

# Let us apply it with a lambda function
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ARTURO', 'CABRERA', 'DEV', 'BLOGGER']
# Lo que realmente hace el mapa es iterar sobre una lista. Por ejemplo, cambia los nombres a mayúsculas y devuelve una nueva lista.

# Python - Filter Function
# La función filter() llama a la función especificada que devuelve un valor booleano para cada elemento de la iterable (lista) especificada. 
# Filtra los elementos que cumplen los criterios de filtrado.
# syntax
filter(function, iterable)

# Ejemplo 1
# Permite filtrar solo nubes pares
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]

# ejemplo 2
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]

# Python - Reduce Function
# La función reduce() está definida en el módulo functools y debemos importarla desde este módulo. 
# Al igual que el mapa y el filtro, toma dos parámetros, una función y un iterable. Sin embargo, no devuelve otro iterable, sino un solo valor.

from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15