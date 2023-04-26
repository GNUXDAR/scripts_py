# EXPRESIONES REGULARES
# Una expresión regular o RegEx es una cadena de texto especial que ayuda a encontrar patrones en los datos.
# Se puede usar un RegEx para verificar si existe algún patrón en un tipo de datos diferente. 
# Para usar RegEx en python primero debemos importar el módulo RegEx que se llama re.
import re
# Después de importar el módulo, podemos usarlo para detectar o encontrar patrones

#  METODOS EN EL MODULO re
# Para encontrar un patrón, usamos un conjunto diferente de conjuntos de caracteres re que permiten buscar una coincidencia en una cadena.
re.match()  # busca solo al comienzo de la primera línea de la cadena y devuelve los objetos coincidentes si los encuentra; de lo contrario, devuelve None.
re.search   # devuelve un objeto de coincidencia si hay uno en cualquier parte de la cadena, incluidas las cadenas de varias líneas.
re.findall  # Devuelve una lista que contiene todas las coincidencias
re.split    # toma una cadena, la divide en los puntos de coincidencia, devuelve una lista
re.sub      # reemplaza una o varias coincidencias dentro de una cadena


# match
# syntax
re.match(substring, string, re.I)
#  substring es una cadena o un patrón, string es el texto que buscamos para un patrón, re.I is case ignore

import re

txt = 'I love to teach python and javaScript'
#  Devuelve un objeto con intervalo y coincidencia
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Vamos a encontrar la posición inicial y final del span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach

import re
txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None

# SEARCH
# syntax
re.match(substring, string, re.I)
# la subcadena es un patrón, la cadena es el texto que buscamos para un patrón, re.I es un indicador de caso ignorado

import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Podemos obtener la posición inicial y final del partido como una tupla usando span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
# Como puede ver, la búsqueda es mucho mejor que la coincidencia porque puede buscar el patrón en todo el texto. 
# La búsqueda devuelve un objeto de coincidencia con una primera coincidencia que se encontró; 
# de lo contrario, devuelve None. Una función mucho mejor es findall. 
# Esta función busca el patrón en toda la cadena y devuelve todas las coincidencias en forma de lista.

# Búsqueda de todas las coincidencias mediante findall
# findall() devuelve todas las coincidencias como una lista
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']

# Como puede ver, la palabra idioma se encontró dos veces en la cadena. Practiquemos un poco más. 
# Ahora buscaremos las palabras Python y python en la cadena:

import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns list
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

# Dado que estamos usando re.I, se incluyen letras minúsculas y mayúsculas. Si no tenemos la bandera re.I, 
# entonces tendremos que escribir nuestro patrón de manera diferente. Vamos a comprobarlo:

import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

# Reemplazo de una subcadena
import re
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
# JavaScript is the most beautiful language that a human being has ever created.
print(match_replaced)
# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
# JavaScript is the most beautiful language that a human being has ever created.
print(match_replaced)

# Añadamos un ejemplo más. La siguiente cadena es muy difícil de leer a menos que eliminemos el símbolo %. 
# Reemplazar el % con una cadena vacía limpiará el texto.

import re

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
# I am teacher and I love teaching.
# There is nothing as rewarding as educating and empowering people.
# I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?

# Dividir texto usando RegEx Split
import re

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt))  # splitting using \n - end of line symbol

# Escribir patrones RegEx
# Para declarar una variable de cadena usamos comillas simples o dobles. Para declarar la variable RegEx r''. 
# El siguiente patrón solo identifica manzana con minúsculas, para que no distinga entre mayúsculas y minúsculas, 
# debemos reescribir nuestro patrón o agregar una bandera.

import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

#  Para hacer que no se distinga entre mayúsculas y minúsculas agregando la bandera '
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# o podemos usar un método de conjunto de caracteres
regex_pattern = r'[Aa]pple' # esto significa que la primera letra podría ser manzana o manzana
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# []: un conjunto de caracteres 
#   [a-c] significa, a ó b ó c 
#   [a-z] significa, cualquier letra de la a a la z 
#   [A-Z] significa, cualquier caracter de la A a la Z 
#   [0-3] significa, 0 ó 1 ó 2 ó 3 
#   [0-9] significa cualquier número del 0 al 9 
#   [A-Za-z0-9] cualquier carácter individual, es decir, de la a a la z, de la A a la Z o del 0 al 9 
# \: utiliza para escapar caracteres especiales 
#   \d significa: coincidencia donde la cadena contiene dígitos (números del 0 al 9) 
#   \D significa: coincidencia donde la cadena no contiene dígitos 
# .: cualquier carácter excepto el carácter de nueva línea (\n) 
# ^: comienza con 
#   r'^subcadena', por ejemplo, r'^amor', una oración que comienza con una palabra amor 
#   r'[^abc] significa no a, no b, no c. 
# $: termina en 
#   r'substring$', por ejemplo, r'love$', oración que termina con una palabra love 
# *: cero o más veces 
#   r'[a]*' significa un opcional o puede ocurrir muchas veces. 
# +: una o más veces 
#   r'[a]+' significa al menos una vez (o más) 
# ?: cero o una vez 
#   r'[a]?' significa cero veces o una vez 
# {3}: exactamente 3 caracteres 
# {3, }: al menos 3 caracteres 
# {3, 8}: de 3 a 8 caracteres 
# | : Cualquiera o 
#   r'apple|banana' significa manzana o plátano 
# (): Captura y grupo

# Usemos ejemplos para aclarar los metacaracteres anteriores:
# Corchete
# Usemos corchetes para incluir mayúsculas y minúsculas

import re
regex_pattern = r'[Aa]pple'  # this square bracket mean either A or a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

# Si queremos buscar el plátano, escribimos el patrón de la siguiente manera:
# this square bracket means either A or a
regex_pattern = r'[Aa]pple|[Bb]anana'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
# Usando el corchete y el operador or , logramos extraer Apple, apple, Banana y banana.

# Carácter de escape (\) en RegEx
import re
regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)    # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], esto no es lo que queremos
print(matches)

# Una o más veces (+)
# d es un carácter especial que significa dígitos, + significa una o más veces
regex_pattern = r'\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - ahora esto es mejor!

# Período(.)
import re

regex_pattern = r'[a].'  # este corchete significa a y . significa cualquier carácter excepto nueva línea
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . cualquier carácter, + cualquier carácter una o más veces
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# Cero o más veces (*)
# Cero o muchas veces. El patrón puede no ocurrir o puede ocurrir muchas veces.
import re
regex_pattern = r'[a].*'  # . cualquier carácter, * cualquier carácter cero o más veces
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']

# Cero o una vez (?)
# Cero o una vez. El patrón puede no ocurrir o puede ocurrir una vez.
import re
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? significa aquí que '-' es opcional
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']

# Cuantificador en RegEx
# Podemos especificar la longitud de la subcadena que estamos buscando en un texto, usando una llave. 
# Imaginemos, nos interesa una subcadena con una longitud de 4 caracteres:
import re
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # exactly four times
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'   # 1 to 4
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']    (no funciona)

# Cart ^
# comienza con
import re
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ significa que comienza con
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']

# Negación
import re
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ en carácter fijo significa negación, no de la A a la Z, no de la a a la z, sin espacio
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']