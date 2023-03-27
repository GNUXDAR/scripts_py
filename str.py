# cadenas de textos
help(str)
refran = "el perro de san roque no tiene rabo "
refran = refran + 'porque ramon rodriguez se lo ha robado'
print(refran)

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
refran.capitalize()             #la primera letra de la cadena en mayuscula
refran.replace('no', 'si')      #remplazar todo del primer parametro por el segundo
refran.find('Roque')            #busca una palabra o un caracter e indica en que posicion esta
refran.find('roque')            #-1 si no la encuentra, distingue mayuscula de minuscula
refran.lower().find('roque')    #pasar a minuscula y buscar la palabra o letra
refran.strip()                  #elimina los espacios del princio y del final
refran.split()                  #crea uan lista con cada elemento de la cadena de texto
refran.split('no')              #parte la cadena en las veces que exista esa palabra o letra, quitando la palabra o letra que se pase por parametro
refran.isupper()                #para determinar si una letra está en mayúscula
refran.islower()                #para determinar si una letra está en minuscula

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
letra = input(" ")  #caracter
print(ord(letra))
print("\nrevertir")
revertir = input("")        #ASCII
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

print(cadena)
print(cadenaCodificada)
print(cadenaDeCodificada)