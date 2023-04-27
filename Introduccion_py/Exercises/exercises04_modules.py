# 00. Escriba una función que genere un random_user_id de seis dígitos/caracteres.
# print(random_user_id());
# '1ee33d'
import random
import string

def random_user_id():
    """ generar una cadena de 6 digitos"""
    # Crear una cadena que contiene letras minúsculas y dígitos numéricos
    choices = string.ascii_lowercase + string.digits
    # Seleccionar aleatoriamente seis caracteres de la cadena
    result = ''.join(random.choice(choices) for i in range(6))
    return result

print(random_user_id())

# 01. Modificar la tarea anterior. Declare una función llamada user_id_gen_by_user. 
# No toma ningún parámetro, pero toma dos entradas usando input(). 
# Una de las entradas es la cantidad de caracteres y la segunda entrada es la cantidad de ID que se supone que se generarán.
def user_id_gen_by_user():
    """ generar N id con N caracteres"""
    cant_char = int(input('Ingrese la cantidad de caracteres: '))
    cant_id = int(input('Ingrese la cantidad de IDs: '))
    choices = string.ascii_lowercase + string.digits
    for id in range(cant_id):
        result_char = ''.join(random.choice(choices) for i in range(cant_char))
        print(result_char)


user_id_gen_by_user()


# 02. Escriba una función list_of_hexa_colors que devuelva cualquier cantidad de colores hexadecimales
# en una matriz (seis números hexadecimales escritos después de #. El sistema de numeración hexadecimal está formado por 16 símbolos, 
# 0-9 y las primeras 6 letras del alfabeto, a-f. 
import random
def list_of_hexa_colors(n):
    colors = []
    for i in range(n):
        color = ''.join([random.choice('0123456789abcdef') for j in range(6)])
        colors.append('#' + color)
    return colors


print(list_of_hexa_colors(6))   # salida: ['#3badae', '#847dda', '#5bdc50', '#845d2f', '#b63a36', '#d116f3']
