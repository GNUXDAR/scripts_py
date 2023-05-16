# un generador de claves, para juegos o programas con seriales
# YORKW-ONMEM-1LBZS-3M89G-UDR14
# 1I7BH-KZOPX-VS1Y9-O5IP2-7BD1V

import random
import string


def key_generator():
    """ generar serial de claves """
    cant_key = int(input('Ingrese la cantidad de Seriales que necesita: '))
    choices = string.ascii_uppercase + string.digits
    for i in range(cant_key):
        key_chars = []
        for j in range(5):
            key_chars.append(''.join(random.choice(choices) for i in range(5)))
        key = '-'.join(key_chars)
        print(key)

key_generator()


