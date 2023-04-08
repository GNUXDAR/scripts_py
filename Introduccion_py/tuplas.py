# tuplas, son como las listas, pero estas no se pueden editar
users = ("Arturo", "gnuxdar")
print(users)

odd_numbers = (1, 3, 5, 7 ,9)
pair_numbers = (2, 4, 6, 8)
print(odd_numbers + pair_numbers)

# como convertir una lista a una tupla
lista = [1, 2]
print(type(lista))

converter = tuple(lista)
print(type(converter))

# en las tuplas se puedehacer todo lo que se hace con una lista, pero que no edite o elimine
menosNumeros = odd_numbers[:2]
print(menosNumeros)
primero, segundo, *otros = odd_numbers
print(primero, segundo, otros)
for n in odd_numbers:
    print(n)

# en tal caso de editar una tupla, esta se tendra que pasar a list, en realidad, se crea una list en base de la tupla
lista_numeros = list(odd_numbers)
lista_numeros[0] = "uno"
print(type(lista_numeros), lista_numeros)