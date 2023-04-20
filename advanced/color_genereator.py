# Escriba una función list_of_hexa_colors que devuelva cualquier cantidad de colores hexadecimales
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
