# LISTAS
# podemos crear listas de dos maneras

# Uso de la función incorporada de lista
# syntax
lst = list()

# usando corchetes
lst = []

# Lista: es una colección ordenada y cambiable (modificable). Permite miembros duplicados.
numeros = [1, 2, 3, 4, 5,]
print(numeros)          # imprime la lista completa
print(numeros[1])       # imprime lo que esta en esa pocion que le pasemos

## lista de string
letras = ["a", "e", "i", "o", "u"]
print(letras)

palabras = ["algo", "esta", "interesante", "oculto", "universidad"]
print(palabras)

web_techs = ['HTML', 'CSS', 'JS', 'React', 'Redux',
             'Node', 'MongDB', 'Python']  # list of web technologies
print('Web technologies:', web_techs)   # Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB', 'Python']
print('Number of Web technologies:', len(web_techs)) # 8
latex_index = len(web_techs) - 1
print(web_techs[latex_index])  # Python


## lista de booleans
booleans = [True, False, True, False]
print(booleans)

## lista de listas
matriz = [[1, 1], [1, 0]]
print(matriz)
 
## unir listas
alfanumericos = numeros + letras
print(alfanumericos)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB', 'PHP']
technologies = front_end + back_end
print(technologies)

## range y list
lista = list(range(1,4))
print(lista)

chars = list("aprendiendo con gnuxdar")
print(chars)

# MANIPULANDO LISTAS
users = ["gnuxdar", "admin", "newbie", "jedi"]
print(users)

users[3] = "yoda"
print(users)
print(users[1:])    # desde la posicion 1 hasta el ultimo
# con negativos (-) va desde el ultimo al primero de la lista, -1, -3, -N
print(users[-1])
# imprimir todos los elemento
print(users[-4:])
# imprime los pares, comeinza desde el inicio y va a (dos) despues: ['gnuxdar', 'newbie']
print(users[::2])
# immprime desde la posicion 1 (el segundo) y luego a cada dos:
print(users[1::2])

numeros = list(range(21))
print(numeros[::2])     # imprime los numero pares de esa list
print(numeros[1::2])    # imprime los numero impares de esa list (inicio::cada tantos numeros)

# DESEMPAQUETAR LISTAS
numeros = [1, 2, 3]

# manera incorrecta!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]
# print(primero, segundo, tercero)  # 1 2 3

primero, segundo, tercero = numeros
# aca se le asigna dinamicamente a cada variable un valor de una posicion
print(primero, segundo, tercero)    # 1 2 3 
print(segundo)                      # podemos acceder al valor de la variable

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# despues de declarar una variable despues de *otros, esta reseva el valor de N variables que se asignen, cada variable es un valor de la lista
primero, *otros, ultimo = numeros
print(primero, ultimo, otros)   # 1 9 [2, 3, 4, 5, 6, 7, 8]

# otro ejemplo
countries = ['Germany', 'France', 'Belgium', 'Sweden',
             'Denmark', 'Finland', 'Norway', 'Iceland', 'España']
gr, fr, bg, sw, *scandic, es = countries
print(gr)   # Germany
print(fr)   # France
print(bg)   # Belgium
print(sw)   # Sweden
print(scandic)  # ['Denmark', 'Finland', 'Norway', 'Iceland']
print(es)   # España


# iterar listas
mascotas = ["zeus", "thitan", "sky"]

for mascota in enumerate(mascotas):
    # Devuelve un objeto de enumeración. iterable debe ser una secuencia, un iterador o algún otro objeto que soporte la iteración.
    # El método __next__() del iterador devuelto por enumerate() devuelve una tupla que contiene un recuento
    # (desde el inicio, que por defecto es 0) y los valores obtenidos al iterar sobre iterable.
    print(mascota)
    # print(mascota[0])  # [0] la posicion de la lista, [1] el valor de la lista

# acceder a los indices de una lista
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)

# buscar el indice de elementos en una lista
mascotas = ["zeus", "titan", "sky", "titan"]
print(mascotas.index("titan"))  # index() muestra el indice del elemento en la lista

# contar elementos de una lista
mascotas = ["zeus", "titan", "sky", "titan"]
print(mascotas.count("titan"))  #count() cuenta, cuantos de esos elementos en la lista hay

if "titan" in mascotas:         #valida si existe en al lista
    print(mascotas.index("titan"))  

# agregando y eliminando elementos de una lista
mascotas = ["zeus", "titan", "sky", "titan"]
mascotas.insert(2, "downie")    # Inserte un nuevo elemento con valor x en la matriz antes de la posición i. Los valores negativos se tratan como relativos al final de la matriz.
mascotas.append("beta")         # inserta un elemento al final de la lista
mascotas.remove("titan")        # elimina la primera coincidencia que exista
mascotas.pop()                  # elimina el ultimo elemento de la lista
mascotas.pop(2)                 # elimina el elemento de la lista, que este en el indice que le pasemos
del mascotas[1]                 # parecido al anterior, pero influye directamente en la posicion o indice
mascotas.clear()                # como su nombre lo indica, limpia por completo la lista
print(mascotas)

# como eliminar varios elementos de una lista
users = ['master prod', 'julian', 'billied', 'forming', 'gabriel77', 'mastergamer',
         'michel', 'mary', 'sandro', 'alexis', 'erick', 'samugamer', 'gogueta', 'hugo']
to_remove = ['julian', 'billied', 'gabriel77',
             'mastergamer', 'michel', 'erick', 'samugamer', 'gogueta', 'hugo']
print(users)
for user in to_remove:
    users.remove(user)
print(users)

# join(): Devuelve una cadena concatenada
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)  # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'


# ordenando listas
numeros = [10, 23, 50, 5, 12, 30]
# numeros.sort()  # ordena la lista original
# numeros.sort(reverse=True)  # ordena la lista de forma descendente
numeros2 = sorted(numeros)  # crea una copia nueva lista ordenada (la mejor opcion)
numeros2 = sorted(numeros, reverse=True)  # tambien podemos ordenarla alreves de la misma manera que antes
print(numeros)
print(numeros2)

# ordenando listas de listas
# siempre y cuando el primer valor de las sublistas sean numeros
users = [
    [1, "admin"],
    [7, "gnuxdar"],
    [5, "grebo"]
    ]
users.sort()
print(users)

# otro metodo para ordenar
users = [
    ["admin", 1],
    ["gnuxdar", 7],
    ["grebo", 5]
]
users.sort(key=lambda el:el[1], reverse=True) # reverse=True es opcional
print(users)

# LISTA DE COMPRENSION
# La comprensión de listas en Python es una forma compacta de crear una lista a partir de una secuencia. 
# Es una forma corta de crear una nueva lista. La comprensión de listas es considerablemente más rápida que procesar una lista usando el bucle for .

# syntax
[i for i in iterable if expression]

# Por ejemplo, si desea cambiar una cadena a una lista de caracteres. Puedes usar un par de métodos. Veamos algunos de ellos:
# One way
language = 'Python'
lst = list(language)  # changing the string to list
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# Second way: list comprehension
lst = [i for i in language]
print(type(lst))  # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']

# Por ejemplo, si desea generar una lista de números
# Generando numeros
numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Es posible hacer operaciones matemáticas durante la iteración
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# También es posible hacer una lista de tuplas
numbers = [(i, i * i) for i in range(11)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
print(numbers)

# La comprensión de listas se puede combinar con la expresión if
# Generando numeros pares
even_numbers = [i for i in range(21) if i % 2 == 0]  # para generar una lista de números pares en el rango de 0 a 21
print(even_numbers)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Generando numeros impares
odd_numbers = [i for i in range(21) if i % 2 != 0]  # para generar números impares en el rango de 0 a 21
print(odd_numbers)

# Filtrar números: filtremos los números pares positivos de la lista a continuación
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Aplanando una matriz tridimensional
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_list for number in row]
print(flattened_list)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

users = [
    ["admin", 1],
    ["gnuxdar", 7],
    ["grebo", 5]
]

# crear un listado de nombres
names = []
for user in users:
    names.append(user[0])
print(names)

# forma mas corta de hacerlo
# names = [expresion for item in items]
names = [user[0] for user in users]
# names = [name[0] for name in names]   # imprimir la primera letra de cada item
print(names)


# Comprobación de un elemento si es miembro de una lista mediante el operador in. Vea el ejemplo a continuación.
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False


# De una lista original, filtrar los elementos que no esten en la segundo lista
user_war = ['crash', 'master pro', 'delvis', 'otto', 'el papu xd', 'lopez', 'espectrohn', 'pata de hierro',
            'hoffman', 'gerardo', 'computer', 'antonio', 'blasete', 'arthurx', 'billied', 'k2', 'destructor',
            'josegAguilera', 'mk', 'ramiro', 'gonazalito', 'andrezvnlza', 'recucus', 'renato cfc', 'andersond',
            'urvina', 'gastonRamos', 'Rey t Torres', 'mary', 'veloz', 'popo', 'hugo_11n', 'samugamer100', 'lopez',
            'alaukabar', 'zaul uwu', 'memosau', 'angel', 'idk lee', '#2']
delete_user = ['lopez', 'espectrohn', 'gonazalito',
               'renato cfc', 'andersond', 'urvina', 'mary', 'veloz', 'popo', 'samugamer100', 'lopez', 'zaul uwu', 'angel', '#2']

user_war = [x for x in user_war if x not in delete_user]
print(user_war)

#FUNCION LAMBDA
# La función Lambda es una pequeña función anónima sin nombre. Puede tomar cualquier número de argumentos, pero solo puede tener una expresión. 
# La función Lambda es similar a las funciones anónimas en JavaScript. Lo necesitamos cuando queremos escribir una función anónima dentro de otra función.
# CREANDO UNA FUNCION LAMBDA
# Para crear una función lambda, usamos la palabra clave lambda seguida de un parámetro, seguido de una expresión. 
# Consulte la sintaxis y el ejemplo a continuación. La función Lambda no usa return pero devuelve explícitamente la expresión.

# syntax
def x(param1, param2, param3): return param1 + param2 + param2
print(x(arg1, arg2, arg3))

# función con nombre
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# Cambiemos la función anterior a una función lambda
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# Función lambda de invocación automática
(lambda a, b: a + b)(2,3) # 5 - necesita encapsularlo en print() para ver el resultado en la consola

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# Multiple variables
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22

# FUNCIÓN LAMBDA DENTRO DE OTRA FUNCIÓN
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32