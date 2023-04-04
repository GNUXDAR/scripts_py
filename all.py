# mostrar mensaje por pantalla
print ("Hola Mundo")


# NUMEROS
numero = 5      # entero -> integer
decimal = 1.2   # float

suma = 10 + 8
resta = 18 - 8
multiplicar = 16*2
dividir = 10 / 2
divicion_sin_decimal = 1 // 3
modulo = 1 % 3
potencia = 2 ** 3

# otra notacion
# numero += 5
# numero -= 3
# numero *= 5
# numero /= 2
numero //= 2


print(dividir)
print(divicion_sin_decimal)
print(modulo)
print(potencia)
print(f"numero  {numero}")

# FUNCIONES MATEMATICAS
# round()  #Devuelve el número redondeado a la precisión de los dígitos después del punto decimal. Si se omite ndigits o es None, devuelve el entero más cercano a su entrada.
print(round(1.3))
print(round(1.5))
print(round(1.7))
# abs() Devuelve el valor absoluto de un número. El argumento puede ser un número entero, un número de coma flotante o un objeto que implemente __abs__(). Si el argumento es un número complejo, se devuelve su magnitud.
print(abs(-44))
print(abs(44))

# COMPARADORES LOGICOS
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)
print(1 == 2)
print(2 == "2")
print(1 != 2)
print(1 != "2")

# capturar valores por pantalla (input) y mostrar
nombre = input('escribe tu nombre ')
print(nombre)

# EJERCICIO: como saber si un anio es bisiesto
print ("Digite el año:")
anio = int(input()) #convertir en entero

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print ("Año bisiesto")

else:
    print ("Año NO bisiesto")

# EJERCICIO: mostrar si el numero ingresao es par o impar
num = input('Introduce un número:')
numInt = int(num)
if (numInt%2==0):
    print('El numero es par')
else:
    print('El numero es impar')

# MOSTRAR LISTA
# range()
for numero in range(5):
    print(numero)

lista = list(range(1, 4))
print(lista)


for numero in range(5):
    print(numero)

# con string
for numero in range(5):
    print(numero, numero * "python ")

# for else
buscar = 2
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print(f"Lo siento, pero no se encontro el numero {buscar}")

# iterar un string
cadena = " esto es una cadena CON espacios "
for letra in cadena:
    print(letra)
    
# BUCLES
# contar una lista
lista = [9, 13, 2, 7, 124, -5]
print (len(lista))

## EJERCICIO: como se haria sin la funcion len?
canList = 0
for elemento in lista:
    canList += 1
    print (f'El elemento que estamos añadiendo es {elemento} y ocupa el orden {canList}')
print(f'El resultado final es {canList}')
print('----------------------------')

## EJERCICIO: sumar los valores de una lista
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
miTexto.title()     # lo mismo que en lo anterior
miTexto.replace('san','mr')  #replazar palabras
miTexto.replace('san','mr').title()


# CADENAS DE TEXTOS
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

# FUNCIONES MAS USADAS CON CADENAS DE CARACTERES
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

test = "1--2--3--4--5"
# split() puede seleccionar la posición en una cadena desde el frente para dividir.
print(test.split("--", 2))
# rsplit() puede seleccionar la posición en una cadena desde atrás para dividir.
print(test.rsplit("--", 2))
# salida
['1', '2', '3--4--5']  # split()
['1--2--3', '4', '5']  # rsplit()

# FORMATEANDO CADENAS
cadena = " esto es una cadena con espacios "
print(cadena)
print(cadena.capitalize())
print(cadena.strip().capitalize())

## EJERCICIOS:
### como podemos extraer la palabra "casa" de la siguiente cadena: "Tengo una casa roja" guardada en la variable frase?
frase = "Tengo una casa roja"
print(frase[frase.find('casa'):frase.find('casa')+len('casa')])

# CONDICIONALES
## if
EDAD = 18
edad_votante = int(input("Ingrese su edad: "))
if edad_votante < EDAD:
    print("No tiene edad para Votar")
if edad_votante >= EDAD:
    print("Felicidades Puede votar")


## else
edad_votante = int(input("Ingrese su edad: "))
if edad_votante < EDAD:
    print("No tiene edad para Votar")
else:
    print("Felicidades Puede votar")

## elif
### es importante que en caso de enteros, se debe evaluar de mayor a menor
edad_cinefilo = int(input("Ingrese su edad cinefilo: "))
if edad_cinefilo > 54:
    print("Puede ver la pelicula con descuento")
elif edad_cinefilo > 17:
    print("Puedes ver la pelicula")
else:
    print("No puedes entrar")
    print("Ve a otro lado")

print("Listo")


## ternario
edad_cinefilo = int(input("Ingrese su edad cinefilo: "))
mensaje = "Puede ver la pelicula" if edad_cinefilo > 18 else "no puedes entrar"
print(mensaje)

# OPERADORES LOGICOS
# and, or, not
gas = False
encendido = True
edad = 18

if gas and encendido and edad > 17:
    print("Puedes avanzar")

if gas or encendido:
    print("Puedes avanzar ve")

if not gas and (encendido and edad > 17):
    print("No Puedes avanzar sin gas")

# tambien se puede hacer de la siguiente manera
edad = 25
if 15 <= edad <= 65:
    print("puede entrar a la piscina")
