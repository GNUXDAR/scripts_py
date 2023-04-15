# Conjunto: es una colección desordenada, no indexada y no modificable, pero podemos agregar nuevos elementos al conjunto. No se permiten miembros duplicados.
# sets: grupo o conjunto
# syntax
st = {}
# or
st = set()

primer = {1,1, 1, 9, 1, 2, 2, 3, 3, 6}
primer.add(10)  # agregar elemento
primer.remove(1)    # eliminar elemento
print(primer)   # {2, 3, 6, 9, 10}

# Agregar múltiples elementos usando update(). El update() permite agregar múltiples elementos a un conjunto. La update () toma un argumento de lista.
tecnologies = {'Vue', 'Laravel', 'Django', 'Flask'}
tecnologies.update(['Html', 'Js', 'CSS'])
# {'Js', 'Laravel', 'CSS', 'Flask', 'Html', 'Django', 'Vue'}
print(tecnologies)

# eliminar elementos de uns set
tecnologies.remove('Django')       # elimina Django

# Los métodos pop() eliminan un elemento aleatorio de una lista y devuelve el elemento eliminado.
tecnologies.pop()

# limpiar elmentos en un set()
tecnologies.clear()  # set()

del tecnologies # eliminar set

# buscar un elemento
tecnologies = {'Vue', 'Laravel', 'Django', 'Flask'}
print('Django' in tecnologies)  # True

# convertir una lista a un set
segundo = [4, 4, 2, 8, 2, 3, 7, 7, 5, 5, 5]
segundo = set(segundo)
print(segundo)

# UNIR SETS
primer = {1, 1, 1, 9, 1, 2, 2, 3, 3, 6}
segundo = [4, 4, 2, 8, 2, 3, 7, 7, 5, 5, 5]
segundo = set(segundo)
print(primer | segundo)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# union() Este método devuelve un nuevo conjunto
primer = {1, 1, 1, 9, 1, 2, 2, 3, 3, 6}
segundo = {4, 4, 2, 8, 2, 3, 7, 7, 5, 5, 5}
tercer = primer.union(segundo)
print(tercer)   # {1, 2, 3, 4, 5, 6, 7, 8, 9}

st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2)  # Los contenidos de st2 se agregan a st1
print(st1)
print(st2)

# interseccion, devuelve lo que se enceuntren en las dos listas
print(primer & segundo)              # {2, 3}
print(primer.intersection(segundo))  # {2, 3}

# diferencia
print(primer - segundo)

# diferencia simetrica
print(primer ^ segundo)
