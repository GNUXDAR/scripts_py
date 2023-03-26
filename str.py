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
refran.capitalize()             #la primera letra de la cadena
refran.replace('no', 'si')      #remplazar todo del primer parametro por l segundo
refran.find('Roque')            #busca una palabra o un caracter e indica en que posicion esta
refran.find('roque')            #-1 si no la encuentra, distingue mayuscula de minuscula
refran.lower().find('roque')    #pasar a minuscula y buscar la palabra o letra
refran.strip()                  #elimina los espacios del rpincio y del final
refran.split()                  #crea uan lista con cada elemento de la cadena de texto
refran.split('no')              #parte la cadena en las veces que exista esa palabra o letra, quitando la palabra o letra que se pase por parametro

# Extraer trosos de una cadena


## ejercicios:
### como podemos extraer la palabra "casa" de la siguiente cadena: "Tengo una casa roja" guardada en la variable frase?
frase = "Tengo una casa roja"
print(frase[frase.find('casa'):frase.find('casa')+len('casa')])
