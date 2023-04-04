## Escribe los divisibles?
### El objeto de esta práctica es realizar un programa que solicite al usuario un número entero positivo e imprima todos los números divisibles entre 5 o 7 
### menores o iguales que el número. Para ello tendréis que utilizar un bucle.

num = input('Introduce un numero:')
numInt = int(num)
for numero in range(0,numInt+1):
    if numero%5==0 or numero%7==0:
        print('El numero', numero, 'cumple con la condicion')

# numInt = 10
# print(list(range(0, 10)))
