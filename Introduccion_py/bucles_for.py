# La vida está llena de rutinas. En programación también hacemos muchas tareas repetitivas. 
# Para manejar tareas repetitivas, los lenguajes de programación usan bucles. 
# El lenguaje de programación Python también proporciona los siguientes tipos de dos bucles: for, while

# resolviendo problemas con bucles

# flujo iterativo
# ---- inicializacion ----
# ---- bucle(for/while) ----
# ---- finalizacion ----

# MOSTRAR LISTA
# range()
for numero in range(5):
    print(numero)

lista = list(range(1, 4))
print(lista)


for numero in range(5):
    print(numero)

## con string
for numero in range(5):
    print(numero, numero * "python ")

## for else
buscar = 2
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print(f"Lo siento, pero no se encontro el numero {buscar}")

## iterar un string
cadena = " esto es una cadena CON espacios "
for letra in cadena:
    print(letra)

## CONTAR UNA LISTA CON FOR
lista = [9, 13, 2, 7, 124, -5]
print (len(lista))

## como se haria sin la funcion len?
canList = 0
for elemento in lista:
    canList += 1
    print (f'El elemento que estamos añadiendo es {elemento} y ocupa el orden {canList}')
print(f'El resultado final es {canList}')
print('----------------------------')

## EJERCICIO: sumar los valores de una lista
lista = [9, 13, 2, 7, 124, -5]
print (sum(lista))
## como se haria sin la funcion sum
suma = 0
for elemento in lista:
    suma = suma + abs(elemento)
    print(f'añadir el elemento {abs(elemento)} y el resultado parcial es {suma}')
print (suma)
print('----------------------------')

## EJERCICIO: calcular la media de los valores de una lista
lista = [9, 13, 2, 7, 124, -5]
print(sum(lista)/len(lista))
## como se haria sin la funcion sum ni len
suma = 0
cuenta = 0
for elemento in lista:
    cuenta += 1
    suma = suma + elemento
    print(f'el elemento que estamos introduciendo es {elemento}')
    print(f'actualmente vamos por el elemento {cuenta}')
    print(f'el resultado parcial de la suma es {suma}')
print(suma/cuenta)

## EJERCICIO: verificar si existe un elemento en una lista
lista = [9, 13, 2, 7, 124, -5, 7]
print(7 in lista)
## como se haria sin la funcion in
existe = False
valor = 7
cuenta = 0
for elemento in lista:
    print(f'estamos en el elemento {elemento}')
    if elemento == valor:
        existe = True
        cuenta += 1
print(existe, cuenta)

## EJERCICIO: como identificar el mayor y menor elemento de una lista
lista = [9, 13, 2, 7, 124, -5, 7]
print(max(lista))
print(min(lista))
## como se haria sin la funcion min y max
mayor = None
menor = None

for elemento in lista:
    if mayor == None or menor == None:
        mayor = elemento
        menor = elemento
    else:
        if elemento > mayor:
            mayor = elemento
        if elemento < menor:
            menor = elemento
print(f' el elemento mayor es {mayor}')
print(f'el elemento menor es {menor}')

# for con una tupla
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)

# for con diccionario
person = {
    'first_name': 'Arturo',
    'last_name': 'Cabrera',
    'age': 404,
    'country': 'Venezuela',
    'is_marred': True,
    'skills': ['PHP', 'Laravel', 'React', 'Flask', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '01010101'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value)  # 

# for con set
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon', 'AC Tecnology'}
for company in it_companies:
    print(company)
