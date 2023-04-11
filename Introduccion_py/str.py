# cadenas de textos
help(str)
refran = "el perro de san roque no tiene rabo "
refran = refran + 'porque ramon rodriguez se lo ha robado'  #concatenacion
print(refran)
print(refran*2) #lo repite * cuantas veces se le indique


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

# invertir una cadena
print(refran[::-1])

# Saltando caracteres al cortar
# Es posible omitir caracteres durante el corte pasando el argumento de paso al método de corte.
language = 'Python'
pto = language[0:6:2]
print(pto)  # Pto

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
## salida
['1', '2', '3--4--5']  # split()
['1--2--3', '4', '5']  # rsplit()

## Ejemplo de uso de formatear cadenas
cadena = " esto es una cadena con espacios "
print(cadena)
print(cadena.capitalize())
print(cadena.strip().capitalize())

## Ejemplo: de isupper y islower
def cambiaMayus(cadena):
    # cambia mayusculas por minusculas y viceversa
    resultado = ""
    for letra in cadena:
        if letra.isupper():
            resultado += letra.lower()
        elif letra.islower():
            resultado += letra.upper()
        else:
            resultado += letra
    print(resultado) 

cambiaMayus('Castilla')

# Formato de cadena de estilo antiguo (% operador)
# En Python hay muchas formas de formatear cadenas.
# En esta sección, cubriremos algunos de ellos. El operador "%"
# se utiliza para formatear un conjunto de variables encerradas en una "tupla" (una lista de tamaño fijo),
# junto con una cadena de formato, que contiene texto normal junto con "especificadores de argumento",
# símbolos especiales como "%s" , "%d", "%f", "%.número de dígitosf".

# %s - Cadena(o cualquier objeto con una representación de cadena, como números)
# %d - Enteros
# %f - Números de punto flotante
# "%.number of digitsf" - Números de punto flotante con precisión fija

# Strings only
first_name = 'Arturo'
last_name = 'Cabrera'
language = 'Python'
formated_string = 'I am %s %s. I am learning %s' % (
    first_name, last_name, language)
print(formated_string)

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.3f.' % (
    radius, area)
print(formated_string)

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib', 'Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string)

# Nuevo formato de cadena de estilo (str.format)
# esta version se introdujo en la version 3
first_name = 'Arturo'
last_name = 'Cabrera'
language = 'Python'
formated_string = 'I am {} {}. I am learning {}'.format(
    first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
# limits it to two digits after decimal
print('{} / {} = {:.2f}'.format(a, b, a / b))
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# Strings  and numbers
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(
    radius, area)  # 2 digits after decimal
print(formated_string)

# Interpolación de cadenas / f-Strings (Python 3.6+)
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')

# Cadenas de Python como secuencias de caracteres
# Las cadenas de Python son secuencias de caracteres y 
# comparten sus métodos básicos de acceso con otras secuencias 
# de objetos ordenadas de Python: listas y tuplas. 
# La forma más sencilla de extraer caracteres individuales de cadenas (y miembros individuales de cualquier secuencia) 
# es descomprimirlos en las variables correspondientes.
language = 'Python'
a, b, c, d, e, f = language  # unpacking sequence characters into variables
print(a)  # P
print(b)  # y
print(c)  # t
print(d)  # h
print(e)  # o
print(f)  # n

# Acceso a caracteres en cadenas por índice
language = 'Python'
first_letter = language[0]
print(first_letter)  # P
second_letter = language[1]
print(second_letter)  # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)  # n

# Si queremos comenzar desde el extremo derecho, podemos usar la indexación negativa. -1 es el último índice.
language = 'Python'
last_letter = language[-1]
print(last_letter)  # n
second_last = language[-2]
print(second_last)  # o


# Extraer trosos de una cadena


## ejercicios:
### como podemos extraer la palabra "casa" de la siguiente cadena: "Tengo una casa roja" guardada en la variable frase?
frase = "Tengo una casa roja"
print(frase[frase.find('casa'):frase.find('casa')+len('casa')])

# Codigo de caracteres 
letra = "a"
print(ord(letra))   #ASCII
print(chr(43))      #convierte de codigo a caracter

## convertir caracter a ascii y vicebersa
letra = input("convertir caracter a ascii ")  #caracter
print(ord(letra))
print("\nrevertir")
revertir = input("convertir ascii a caracter")        #ASCII
revertir = int(revertir)
print(chr(revertir))      #convierte de codigo a caracter


cadena = "El perro de Roque"
for letra in cadena:
    print(ord(letra), end=" ") #con "end" manipulamos el print para que lo imprima en la msiam linea con una espacio

## podemos utilizar esta forma de almacenar los caracteres para encriptar un mensaje de forma sencilla con una encriptacion por deplazamiento
## tambien conocida como cifrado cesar
# cifrado y descifrado
cadena="Sigueme en mis redes con el usuario gnuxdar"
cadenaCodificada=''
desplazamiento=7

for letra in cadena:
    cadenaCodificada = cadenaCodificada+chr(ord(letra)+desplazamiento)
cadenaDeCodificada=''

for letra in cadenaCodificada:
    cadenaDeCodificada=cadenaDeCodificada+chr(ord(letra)-desplazamiento)

print(cadenaCodificada)
print(cadenaDeCodificada)