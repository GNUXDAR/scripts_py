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
refran.swapcase()               # Convierte todos los caracteres en mayúsculas a minúsculas y todos los caracteres en minúsculas a caracteres en mayúsculas
refran.capitalize()             #la primera letra de la cadena en mayuscula
str.title(refran)               # poner el principio de cada palabra en mayuscula
refran.title()                  # lo mismo que en lo anterior
refran.replace('no', 'si')      #remplazar todo del primer parametro por el segundo
refran.find('Roque')            #busca una palabra o un caracter e indica en que posicion esta, devuelve el indice de la primera aparicion
refran.find('roque')            #-1 si no la encuentra, distingue mayuscula de minuscula
refran.rfind()                  # Devuelve el índice de la última aparición de una subcadena, si no se encuentra devuelve -1
print("rabo" in refran)         #busca si existe
print("rabo" not in refran)     #busca si no existe
refran.lower().find('roque')    #pasar a minuscula y buscar la palabra o letra
refran.strip()                  #elimina los espacios del princio y del final y los saltos de lineas
refran.rstrip()                 # elimina los espacios de la derecha
refran.lstrip()                 # elimina los espacios de la izquierda
refran.split()                  #crea uan lista con cada elemento de la cadena de texto
refran.split('no')              #parte la cadena en las veces que exista esa palabra o letra, quitando la palabra o letra que se pase por parametro
refran.isupper()                #Comprueba si todos los caracteres del alfabeto en la cadena están en mayusculas
refran.islower()                #Comprueba si todos los caracteres del alfabeto en la cadena están en minúsculas
refran.startswith('El perro')   # comprueba si la cadena comienza con la cadena especificada


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

## count() contando caracteres en eun string
# count(): devuelve ocurrencias de subcadena en cadena, cuenta(subcadena, inicio=.., final=..).
# El inicio es una indexación inicial para contar y el final es el último índice para contar.
refran = '''el perro de san roque no tiene rabo 
        porque ramon rodriguez se lo ha robado, 
        esto es un refran tipico de España. ole toro'''
print(refran.count('de'))
print(refran.count('de', 8, 20))

## endswith(): comprueba si una cadena termina con un final específico
challenge = 'programming with python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion'))  # False

# expandtabs(): reemplaza el carácter de tabulación con espacios, el tamaño de tabulación predeterminado es 8. Toma el argumento de tamaño de tabulación
# no es muy exacta Oo
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
# todo lo anterior es mejor con: cadena.swapcase()

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
formated_string = 'I am {} {}. I am learning {}'.format(first_name, last_name, language)
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