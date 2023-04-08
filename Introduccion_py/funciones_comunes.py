# Funciones mas usadas con cadenas de caracteres
print(refran.upper())
refran.lower()                  #todas a minusculas
refran.upper()                  #todas a mayusculas
refran.capitalize()             #la primera letra de la cadena en mayuscula
str.title(refran)               # poner el principio de cada palabra en mayuscula
refran.title()                  # lo mismo que en lo anterior
refran.replace('no', 'si')      #remplazar todo del primer parametro por el segundo
refran.find('Roque')            #busca una palabra o un caracter e indica en que posicion esta
refran.find('roque')            #-1 si no la encuentra, distingue mayuscula de minuscula
print("rabo" in refran)         #busca si existe
print("rabo" not in refran)     #busca si no existe
refran.lower().find('roque')    #pasar a minuscula y buscar la palabra o letra
refran.strip()                  #elimina los espacios del princio y del final y los saltos de lineas
refran.rstrip()                 # elimina los espacios de la derecha
refran.lstrip()                 # elimina los espacios de la izquierda
refran.split()                  #crea uan lista con cada elemento de la cadena de texto
refran.split('no')              #parte la cadena en las veces que exista esa palabra o letra, quitando la palabra o letra que se pase por parametro
refran.isupper()                #para determinar si una letra está en mayúscula
refran.islower()                #para determinar si una letra está en minuscula

test = "1--2--3--4--5"
print(test.split("--", 2))      # split() puede seleccionar la posición en una cadena desde el frente para dividir.
print(test.rsplit("--", 2))     # rsplit() puede seleccionar la posición en una cadena desde atrás para dividir.

mascotas = ["zeus", "thitan", "sky"]
for mascota in enumerate(mascotas):
    print(mascota)
    # enumerate() Devuelve un objeto de enumeración. iterable debe ser una secuencia, un iterador o algún otro objeto que soporte la iteración.
    # El método __next__() del iterador devuelto por enumerate() devuelve una tupla que contiene un recuento
    # (desde el inicio, que por defecto es 0) y los valores obtenidos al iterar sobre iterable.

mascotas = ["zeus", "titan", "sky", "titan"]
print(mascotas.index("titan"))          # index() muestra el indice del elemento en la lista; list.py

# agregando y eliminando elementos de una lista
mascotas = ["zeus", "titan", "sky", "titan"]
# Inserte un nuevo elemento con valor x en la matriz antes de la posición i. Los valores negativos se tratan como relativos al final de la matriz.
mascotas.insert(2, "downie")
mascotas.append("beta")         # inserta un elemento al final de la lista
mascotas.remove("titan")        # elimina la primera coincidencia que exista
mascotas.pop()                  # elimina el ultimo elemento de la lista
# elimina el elemento de la lista, que este en el indice que le pasemos
mascotas.pop(2)
# parecido al anterior, pero influye directamente en la posicion o indice
del mascotas[1]
mascotas.clear()                # como su nombre lo indica, limpia por completo la lista
print(mascotas)

# ordenando listas
numeros = [10, 23, 50, 5, 12, 30]
# numeros.sort()  # ordena la lista
# numeros.sort(reverse=True)  # ordena la lista de forma descendente
numeros2 = sorted(numeros)  # crea una copia nueva lista
numeros2 = sorted(numeros, reverse=True)  # tambien podemos ordenarla alreves de la misma manera que antes
lambda  #fucnciones anonimas