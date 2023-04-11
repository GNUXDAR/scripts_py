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
print(refran.count('de'))
print(refran.count('de', 8, 20))

test = "1--2--3--4--5"
print(test.split("--", 2))      # split() puede seleccionar la posición en una cadena desde el frente para dividir.
print(test.rsplit("--", 2))     # rsplit() puede seleccionar la posición en una cadena desde atrás para dividir.

# endswith(): comprueba si una cadena termina con un final específico
challenge = 'programming with python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False

# expandtabs(): reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación
challenge = 'i\tam\tlearning\tpython'
print(challenge.expandtabs())           # 'i       am      learning        python'
print(challenge.expandtabs(10))          # 'i         am        learning  python'

# index (): devuelve el índice más bajo de una subcadena, los argumentos adicionales indican el índice inicial y final
# (predeterminado 0 y longitud de cadena - 1). Si no se encuentra la subcadena, genera un valueError.
challenge = 'i am learning python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 4))  # error

# rindex(): Devuelve el índice más alto de una subcadena, los argumentos adicionales indican el índice inicial y final (predeterminado 0 y longitud de la cadena - 1)
challenge = 'i am learning python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 8
print(challenge.rindex(sub_string, 9))  # error

# isalnum(): comprueba el carácter alfanumérico
challenge = 'ThirtyDaysPython'
print(challenge.isalnum())  # True

challenge = '30DaysPython'
print(challenge.isalnum())  # True

challenge = 'i am learning python'
print(challenge.isalnum())  # False, space is not an alphanumeric character

challenge = 'i am learning python 2019'
print(challenge.isalnum())  # False

# isalpha(): Comprueba si todos los elementos de la cadena son caracteres alfabéticos (a-z y A-Z)
challenge = 'i am learning python'
print(challenge.isalpha())  # False, space is once again excluded
challenge = 'ThirtyDaysPython'
print(challenge.isalpha())  # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): comprueba si todos los caracteres de una cadena son decimales (0-9)
challenge = 'i am learning python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdecimal())   # False
challenge = '12 3'
print(challenge.isdecimal())  # False, espacio no permitido

# isdigit(): comprueba si todos los caracteres de una cadena son números(0-9 y algunos otros caracteres Unicode para números)
challenge = 'Thirty'
print(challenge.isdigit())  # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True

# isnumeric(): comprueba si todos los caracteres de una cadena son números o están relacionados con números (al igual que isdigit(), solo acepta más símbolos, como ½)
num = '10'
print(num.isnumeric())  # True
num = '\u00BD'  # ½
print(num.isnumeric())  # True
num = '10.5'
print(num.isnumeric())  # False

# isidentifier(): busca un identificador válido; verifica si una cadena es un nombre de variable válido
challenge = '30DaysOfPython'
print(challenge.isidentifier())  # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier())  # True

# join(): Devuelve una cadena concatenada
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result)  # 'HTML CSS JavaScript React'
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'


mascotas = ["zeus", "thitan", "sky"]
for mascota in enumerate(mascotas):
    print(mascota)
    # enumerate() Devuelve un objeto de enumeración. iterable debe ser una secuencia, un iterador o algún otro objeto que soporte la iteración.
    # El método __next__() del iterador devuelto por enumerate() devuelve una tupla que contiene un recuento
    # (desde el inicio, que por defecto es 0) y los valores obtenidos al iterar sobre iterable.

mascotas = ["zeus", "titan", "sky", "titan"]
print(mascotas.index("titan"))          # index() muestra el indice del elemento en la lista; list.py

# agregando y eliminando elementos de una lista
lista = [9, 13, 2, 7, 124, -5]
print(sum(lista))
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