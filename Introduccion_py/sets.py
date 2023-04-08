# sets: grupo o conjunto
primer = {1,1, 1, 9, 1, 2, 2, 3, 3, 6}
primer.add(10)
primer.remove(1)
print(primer)

# convertir una lista a un set
segundo = [4, 4, 2, 8, 2, 3, 7, 7, 5, 5, 5]
segundo = set(segundo)
print(segundo)

# unir sets
print(primer | segundo)


# interseccion, devuelve lo que se enceuntren en las dos listas
print(primer & segundo)

# diferencia
print(primer - segundo)

# diferencia simetrica
print(primer ^ segundo)
