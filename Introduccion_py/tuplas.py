# Tupla: Una tupla es una colección de diferentes tipos de datos que está ordenada e inmutable (no cambiable). 
# Las tuplas se escriben con paréntesis (). Una vez que se crea una tupla, no podemos cambiar sus valores. 
# No podemos usar métodos como add, insert, remove en una tupla porque no es modificable (mutable). 
# A diferencia de la lista, la tupla tiene pocos métodos. Métodos relacionados con las tuplas:

# tuple(): para crear una tupla vacía
# count(): para contar el número de un elemento especificado en una tupla
# index(): para encontrar el índice de un elemento especificado en una tupla
# operador: para unir dos o más tuplas y crear una nueva tupla.
# tuplas, son como las listas, pero estas no se pueden editar

# CREANDO TUPLAS
empty_tuple = ()
empty_tuple = tuple()

users = ('Arturo', 'gnuxdar')
print(users)

odd_numbers = (1, 3, 5, 7 ,9)
pair_numbers = (2, 4, 6, 8)
print(odd_numbers + pair_numbers)   # (1, 3, 5, 7, 9, 2, 4, 6, 8)
print(tuple(sorted(odd_numbers + pair_numbers)))    # ordenar tuplas, se pasa a lista ordenada con sorted y luego se pasa a tupla: (1, 2, 3, 4, 5, 6, 7, 8, 9)

# como convertir una lista a una tupla
lista = [1, 2]
print(type(lista))

converter = tuple(lista)
print(type(converter))

# en las tuplas se puede hacer todo lo que se hace con una lista, pero que no edite o elimine
menosNumeros = odd_numbers[:2]
print(menosNumeros)
primero, segundo, *otros = odd_numbers
print(primero, segundo, otros)
for n in odd_numbers:
    print(n)

# verificar elementos en una tupla
tecnologies = ('React', 'Python', 'HTML', 'CSS')
print('Python' in tecnologies)  # True

# en tal caso de editar una tupla, esta se tendra que pasar a list, en realidad, se crea una list en base de la tupla
lista_numeros = list(odd_numbers)
lista_numeros[0] = 'uno'
print(type(lista_numeros), lista_numeros)

# Usamos el método len() para obtener la longitud de una tupla.
tecnologies = ('React', 'Python', 'HTML', 'CSS')
print(len(tecnologies)) # 4 es la cantidad de elementos en la tupla

# Cortando tuplas
print(tecnologies[0:2])  # ('React', 'Python')
print(tecnologies[0:])  # todosl los items

# No es posible eliminar un solo elemento en una tupla, pero es posible eliminar la tupla en sí usando del.
del tecnologies
print(tecnologies)
