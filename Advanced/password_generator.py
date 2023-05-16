# No toma ningún parámetro, pero toma dos entradas usando input().
# Una de las entradas es la cantidad de caracteres y la segunda entrada es la cantidad de ID que se supone que se generarán.

import random
import string


def user_id_gen_by_user():
    """ generar una password dificil de descifrar"""
    cant_char = int(input('Ingrese la cantidad de caracteres: '))
    cant_id = 1 # int(input('Ingrese la cantidad de IDs: '))
    choices = string.punctuation + string.digits
    for id in range(cant_id):
        result_char = ''.join(random.choice(choices) for i in range(cant_char))
        print(result_char)


user_id_gen_by_user()
