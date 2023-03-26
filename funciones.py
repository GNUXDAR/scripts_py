# funciones en python
def mifuncion():
    print(f'---- FUNCIONES ----')
    print(f'vamos a sumar dos numeros 5 + 5: {5+5}')
mifuncion()

# funciones con parametros
def mifuncionParam(num1, num2):
    print(f'---- FUNCIONES CON PARAMETROS ----')
    print(f'el resultado de la suma de sus dos numeros es {num1+num2}')

mifuncionParam(5, 5)

# funcion con return
def suma(num1, num2):
    total = num1 + num2
    return total

# funciones desde objetos
miTexto = "el perro de san roque no tiene rabo"
help(str)
str.title(miTexto)  #poner el principio de cada palabra en mayuscula
mitexto.title()     # lo mismo que en lo anterior
mitexto.replace('san','mr')  #replazar palabras
mitexto.replace('san','mr').title() 