# xargs es poder pasarle N argumentos a la funcion
def suma(*numeros):
    result = 0
    for numero in numeros:
        result += numero
    print(result)


suma(2, 5)
suma(3, 4, 3)
