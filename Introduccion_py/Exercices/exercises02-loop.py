# 00. Itere de 0 a 10 usando el bucle for, haga lo mismo usando el bucle while.
for i in range(11):
    print(i)

i = 0
while i < 11:
    print(i)
    i += 1

# 01. Itere de 10 a 0 usando el bucle for, haga lo mismo usando el bucle while.
for i in range(10, -1, -1): # desde el 10 hasta el -1 sin incluir, osea el 0
    print(i)


i = 10
while i >= 0:
    print(i)
    i -= 1

# 02.Escriba un bucle que haga siete llamadas a print(), 
# de modo que obtengamos en la salida el siguiente triángulo:
  #
  ##
  ###
  ####
  #####
  ######
  #######

for i in range(8):
    print('#'*i)

# 03.Use bucles anidados para crear lo siguiente:
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8):
    for j in range(8):
        print("# ", end='')
    print()

# 04. Imprime el siguiente patrón:
# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
for i in range(11):
    result = i * i
    print(f'{i} x {i} = {result}')

# 05. Iterar a través de la lista, ['Python', 'Numpy', 'Pandas', 'Django', 'Flask'] usando un bucle for e imprimir los elementos.
technologies = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for i in technologies:
    print(i)

# 06. Use for loop para iterar de 0 a 100 e imprimir solo números pares
for i in range(101):
    if i % 2 == 0:
        print(i)

# 07. Use for loop para iterar de 0 a 100 e imprimir solo números impares
for i in range(101):
    if i % 2 != 0:
        print(i)

# 08. Use for loop para iterar de 0 a 100 e imprimir la suma de todos los números: 5050.
result = 0
for i in range(101):
    result += i
print(result)

# 09. Use for loop para iterar de 0 a 100 e imprimir la suma de todos los pares y la suma de todos los impares: 2550 y 2550
result_pares = 0
result_impares = 0
for i in range(101):
    if i % 2 == 0:
        result_pares += i
    if i % 2 != 0:
        result_impares += i
print(result_pares)
print(result_impares)


# 10. Esta es una lista de frutas, ['plátano', 'naranja', 'mango', 'limón'] invierta el orden usando bucle.
frutas = ['plátano', 'naranja', 'mango', 'limón']
frutas_revertidas = frutas[::-1]
print(frutas_revertidas)  # salida: ['limón', 'mango', 'naranja', 'plátano']

fruits = ['plátano', 'naranja', 'mango', 'limón']
new_fruits = list()
size = len(fruits)
for i in fruits:
    new_fruits.insert(0, i)
print(new_fruits)
