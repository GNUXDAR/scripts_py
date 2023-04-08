# funciones en python
def mifuncion():
    """ imprime un string """
    print('---- FUNCIONES ----')
    print(f'vamos a sumar dos numeros 5 + 5: {5+5}')


mifuncion()

# funciones con parametros
def mifuncion_param(num1, num2):
    """ funcion con dos parametros """
    print('---- FUNCIONES CON PARAMETROS ----')
    print(f'el resultado de la suma de sus dos numeros es {num1+num2}')


mifuncion_param(5, 5)

# funcion con return
def suma(num1, num2):
    """ funcion con return """
    total = num1 + num2
    return total


valor_de_suma = suma(5, 5)
print(valor_de_suma)


# funciones desde objetos
miTexto = "el perro de san roque no tiene rabo"
help(str)
str.title(miTexto)  # poner el principio de cada palabra en mayuscula
mitexto.title()     # lo mismo que en lo anterior
mitexto.replace('san', 'mr')  # replazar palabras
mitexto.replace('san', 'mr').title()

# parametros opcionales
def imprime_cliente(nombre="Arturo", apellido="Cabrera"):
    """ funcio con parametros opcionales """
    print(f"El nombre del cliente es {nombre} {apellido}")


imprime_cliente("Adrian", "Guillermo")

# argumentos nombrados
def imprime_user(nombre="Arturo", apellido="Cabrera"):
    """ funcion con argumentos nombrados"""
    print(f"El nombre del cliente es {nombre} {apellido}")


imprime_user(apellido="Guerrero", nombre="Brunilde")
