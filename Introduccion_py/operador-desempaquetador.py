lista1 = [1, 2, 3, 4, 5]
print(1, 2, 3, 4, 5)
print(*lista1)

lista2 = [5, 6, 7, 8]
combinada = ["Hola", *lista1, "Mundo", *lista2, "otra cosa"]
print(combinada)

# con diccionarios
punto1 = {"x": 19}
punto2 = {"y": 33}

nuevo_punto = {**punto1, **punto2}
print(nuevo_punto)

nuevo_punto2 = {**punto1, **punto2, "z": 25}
print(nuevo_punto2)

nuevo_punto3 = {**punto1, "h": 12, **punto2, "z": 25}   # insertando valores
print(nuevo_punto3)


nuevo_punto4 = {**punto1, "x": 12, **punto2, "z": 25}   # ccambiando valores, cuando consigue un valor de llaves iguales, asignara el valor de la llave que este mas a ala izquierda al de la derecha
print(nuevo_punto4)
