# LISTAS
numeros = [1, 2, 3, 4, 5,]
print(numeros)          # imprime la lista completa
print(numeros[1])       # imprime lo que esta en esa pocion que le pasemos

## lista de string
letras = ["a", "e", "i", "o", "u"]
print(letras)

palabras = ["algo", "esta", "interesante", "oculto", "universidad"]
print(palabras)

## lista de booleans
booleans = [True, False, True, False]
print(booleans)

## lista de listaspalabras
matriz = [[1, 1], [1, 0]]
print(matriz)
 
## unir listas
alfanumericos = numeros + letras
print(alfanumericos)

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
# print(primero, segundo, tercero)

primero, segundo, tercero = numeros
# aca se le asigna dinamicamente a cada variable un valor de una posicion
print(primero, segundo, tercero)
print(segundo)                      # podemos acceder al valor de la variable

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# despues de declarar una variable despues de *otros, esta reseva el valor de N variables que se asignen, cada variable es un valor de la lista
primero, *otros, ultimo = numeros
print(primero, ultimo, otros)

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

# ordenando listas
numeros = [10, 23, 50, 5, 12, 30]
# numeros.sort()  # ordena la lista
# numeros.sort(reverse=True)  # ordena la lista de forma descendente
numeros2 = sorted(numeros)  # crea una copia nueva lista
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

# listas de comprension
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
