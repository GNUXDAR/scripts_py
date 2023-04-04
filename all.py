# mostrar mensaje por pantalla
print ("Hola Mundo");

# capturar valores por pantalla (input) y mostrar
nombre = input('escribe tu nombre ')
print(nombre)

# como saber si un anio es bisiesto
print ("Digite el año:")
anio = int(input()) #convertir en entero

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print ("Año bisiesto")

else:
    print ("Año NO bisiesto")

# mostrar si el numero ingresao es pas o impar
num = input('Introduce un número:')
numInt = int(num)
if (numInt%2==0):
    print('El numero es par')
else:
    print('El numero es impar')

# mostrar una lista
lista = list(range(1,4))
print(lista)

# BUCLES
# contar una lista
lista = [9, 13, 2, 7, 124, -5]
print (len(lista))

## como se haria sin la funcion len?
canList = 0
for elemento in lista:
    canList += 1
    print (f'El elemento que estamos añadiendo es {elemento} y ocupa el orden {canList}')
print(f'El resultado final es {canList}')
print('----------------------------')

## sumar los valores de una lista
lista = [9, 13, 2, 7, 124, -5]
print (sum(lista))
## como se haria sin la funcion sum
suma = 0
for elemento in lista:
    suma = suma + abs(elemento)
    print(f'añadir el elemento {abs(elemento)} y el resultado parcial es {suma}')
print (suma)
print('----------------------------')

## calcular la media de los valores de una lista
lista = [9, 13, 2, 7, 124, -5]
print(sum(lista)/len(lista))
## como se haria sin la funcion sum ni len
suma = 0
cuenta = 0
for elemento in lista:
    cuenta += 1
    suma = suma + elemento
    print(f'el elemento que estamos introduciendo es {elemento}')
    print(f'actualmente vamos por el elemento {cuenta}')
    print(f'el resultado parcial de la suma es {suma}')
print(suma/cuenta)

## verificar si existe un elemento en una lista
lista = [9, 13, 2, 7, 124, -5, 7]
print(7 in lista)
## como se haria sin la funcion in
existe = False
valor = 7
cuenta = 0
for elemento in lista:
    print(f'estamos en el elemento {elemento}')
    if elemento == valor:
        existe = True
        cuenta += 1
print(existe, cuenta)

## como identificar el mayor y menor elemento de una lista
lista = [9, 13, 2, 7, 124, -5, 7]
print(max(lista))
print(min(lista))
## como se haria sin la funcion min y max
mayor = None
menor = None

for elemento in lista:
    if mayor == None or menor == None:
        mayor = elemento
        menor = elemento
    else:
        if elemento > mayor:
            mayor = elemento
        if elemento < menor:
            menor = elemento
print(f' el elemento mayor es {mayor}')
print(f'el elemento menor es {menor}')

# funciones con parametros
def mifuncionParam(num1, num2):
    print(f'---- FUNCIONES CON PARAMETROS ----')
    print(f'el resultado de la suma de sus dos numeros es {num1+num2}')

mifuncionParam(5, 5)


# funcion con return
# def suma(num1, num2):
#     total = num1 + num2
#     return total

# modulos
# cada uno de los archivos .py que generamos en python se denominan modulos, y son considerados contenedores para organizar nuestro codigo

#paquetes
# un pauqete es un modulo que sirve para contener otros modulos y paquetes, en la practica es un directorio que contiene un archivo '__init__.py
# dentro de dicho directorio podremos tener almacenados otros modulos o paquetes
# .
# |-- modulo1.py
# |-- paquete
#   |-- __init__.py
#   |-- modulo1.py
#   |-- subpaquete
#       |-- __init__.py
#       |-- modulo1.py
#       |-- modulo2.py


import math
help(math) # mostrar la descripcion de la libreria
print(math.cos(math.pi))  #coseno de pi

# funciones desde objetos
miTexto = "el perro de san roque no tiene rabo"
help(str)
str.title(miTexto)  #poner el principio de cada palabra en mayuscula
mitexto.title()     # lo mismo que en lo anterior
mitexto.replace('san','mr')  #replazar palabras
mitexto.replace('san','mr').title()


# cadenas de textos
refran = "el perro de san roque no tiene rabo "
refran = refran + 'porque ramon rodriguez se lo ha robado'
print(refran)
print(refran*2)  # lo repite * cuantas veces se le indique

## la \ nos ayuda a organizarnos
refran = "el perro de san roque no tiene rabo "\
        "porque ramon rodriguez se lo ha robado, "\
        "esto es un refran tipico de España."
print(refran)

## la \n es el salto de linea
refran = "el perro de san roque no tiene rabo \n"\
        "porque ramon rodriguez se lo ha robado, \n"\
        "esto es un refran tipico de España."
print(refran)

## el ''' para escribir enb varias lineas e interprete saltos de lineas y espacios
refran = '''el perro de san roque no tiene rabo 
        porque ramon rodriguez se lo ha robado, 
        esto es un refran tipico de España. ole toro'''
print(refran)


# contar el tamaño de la cadena
refran = 'El perro de San Roque no tiene rabo ...'
print(len(refran))  # contar la cadena
print(refran[0])    #posicion 0
print(refran[38])   #posicion final
print(refran[3:21]) #principio - fin
print(refran[:21])  # desde el inicio hasta la posicion indicada de final
print(refran[21:])  # desde la posicion 21 hasta el final de la cadena
print(refran[:-10]) # desde el principio hasta -10 posisciones del final
print(refran[-10:]) # los 10 ultimos caracteres

# Funciones mas usadas con cadenas de caracteres
print(refran.upper())
refran.lower()                  #todas a minusculas
refran.upper()                  #todas a mayusculas
refran.capitalize()             #la primera letra de la cadena
str.title(refran)               # poner el principio de cada palabra en mayuscula
refran.title()                  # lo mismo que en lo anterior
refran.replace('no', 'si')      #remplazar todo del primer parametro por l segundo
refran.find('Roque')            #busca una palabra o un caracter e indica en que posicion esta
refran.find('roque')            #-1 si no la encuentra, distingue mayuscula de minuscula
print("rabo" in refran)         # busca si existe
print("rabo" not in refran)     # busca si no existe
refran.lower().find('roque')    #pasar a minuscula y buscar la palabra o letra
refran.strip()                  #elimina los espacios del rpincio y del final
refran.rstrip()                 # elimina los espacios de la derecha
refran.lstrip()                 # elimina los espacios de la izquierda
refran.split()                  #crea uan lista con cada elemento de la cadena de texto
refran.split('no')              #parte la cadena en las veces que exista esa palabra o letra, quitando la palabra o letra que se pase por parametro
refran.isupper()                #para determinar si una letra está en mayúscula
refran.islower()                #para determinar si una letra está en minuscula

# Ejemplo de uso de formatear cadenas
cadena = " esto es una cadena con espacios "
print(cadena)
print(cadena.capitalize())
print(cadena.strip().capitalize())

# Extraer trosos de una cadena


## ejercicios:
### como podemos extraer la palabra "casa" de la siguiente cadena: "Tengo una casa roja" guardada en la variable frase?
frase = "Tengo una casa roja"
print(frase[frase.find('casa'):frase.find('casa')+len('casa')])
