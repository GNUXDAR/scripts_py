# Una función es un bloque reutilizable de código o declaraciones de programación diseñadas para realizar una determinada tarea. 
# Para definir o declarar una función, Python proporciona la palabra clave def. 
# La siguiente es la sintaxis para definir una función. El bloque de función de código se ejecuta solo si se llama o invoca la función

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


def imprime_cliente(nombre="Arturo", apellido="Cabrera"):
    """ funcio con parametros opcionales """
    customer = f"El nombre del cliente es {nombre} {apellido}"
    return customer

print(imprime_cliente("Adrian", "Guillermo"))   # El nombre del cliente es Adrian Guillermo
print(imprime_cliente())                        # El nombre del cliente es Arturo Cabrera


# funciones desde objetos
miTexto = "el perro de san roque no tiene rabo"
help(str)
str.title(miTexto)  # poner el principio de cada palabra en mayuscula
mitexto.title()     # lo mismo que en lo anterior
mitexto.replace('san', 'mr')  # replazar palabras
mitexto.replace('san', 'mr').title()

# parametros por defecto
def imprime_cliente(nombre="Arturo", apellido="Cabrera"):
    """ funcio con parametros opcionales """
    print(f"El nombre del cliente es {nombre} {apellido}")


imprime_cliente("Adrian", "Guillermo")

# argumentos nombrados
def imprime_user(nombre="Arturo", apellido="Cabrera"):
    """ funcion con argumentos nombrados"""
    print(f"El nombre del cliente es {nombre} {apellido}")


imprime_user(apellido="Guerrero", nombre="Brunilde")
