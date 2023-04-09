# mostrar mensaje por pantalla
print ("Hola Mundo")


# NUMEROS
    numero = 5      # entero -> integer
    decimal = 1.2   # float

    suma = 10 + 8
    resta = 18 - 8
    multiplicar = 16*2
    dividir = 10 / 2
    divicion_sin_decimal = 1 // 3
    modulo = 1 % 3
    potencia = 2 ** 3

    # otra notacion
    # numero += 5
    # numero -= 3
    # numero *= 5
    # numero /= 2
    numero //= 2


    print(dividir)
    print(divicion_sin_decimal)
    print(modulo)
    print(potencia)
    print(f"numero  {numero}")

# FUNCIONES MATEMATICAS
    # round()  #Devuelve el número redondeado a la precisión de los dígitos después del punto decimal. Si se omite ndigits o es None, devuelve el entero más cercano a su entrada.
    print(round(1.3))
    print(round(1.5))
    print(round(1.7))
    # abs() Devuelve el valor absoluto de un número. El argumento puede ser un número entero, un número de coma flotante o un objeto que implemente __abs__(). Si el argumento es un número complejo, se devuelve su magnitud.
    print(abs(-44))
    print(abs(44))

# COMPARADORES LOGICOS
    print(1 < 2)
    print(1 > 2)
    print(1 <= 2)
    print(1 >= 2)
    print(1 == 2)
    print(2 == "2")
    print(1 != 2)
    print(1 != "2")

# capturar valores por pantalla (input) y mostrar
    nombre = input('escribe tu nombre ')
    print(nombre)

# EJERCICIO: como saber si un anio es bisiesto
print ("Digite el año:")
anio = int(input()) #convertir en entero

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print ("Año bisiesto")

else:
    print ("Año NO bisiesto")

# EJERCICIO: mostrar si el numero ingresao es par o impar
num = input('Introduce un número:')
numInt = int(num)
if (numInt%2==0):
    print('El numero es par')
else:
    print('El numero es impar')

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


# BUCLES
## while
    numero = 1
    while numero < 100:
        print(numero)
        numero *= 2

    comando = ""
    while comando.lower() != "salir":
        comando = input("$ ")
        print(comando)

    # while infinito
    while True:
        comando = input("$ ")
        print(comando)
        if comando.lower() == "exit":
            break

# contar una lista
    lista = [9, 13, 2, 7, 124, -5]
    print (len(lista))

## EJERCICIO: como se haria sin la funcion len?
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

## calcular la media de los valores de una lista
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

## verificar si existe un elemento en una lista
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

## como identificar el mayor y menor elemento de una lista
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

#funciones
    # funciones con parametros
    def mifuncionParam(num1, num2):
        print(f'---- FUNCIONES CON PARAMETROS ----')
        print(f'el resultado de la suma de sus dos numeros es {num1+num2}')

    mifuncionParam(5, 5)


    # funcion con return
    def suma(num1, num2):
        total = num1 + num2
        return total


    valor_de_suma = suma(5, 5)
    print(valor_de_suma)

    # parametros opcionales
    def imprime_cliente(nombre="Arturo", apellido="Cabrera"):
        print(f"El nombre del cliente es {nombre} {apellido}")


    imprime_cliente("Adrian", "Guillermo")

    # argumentos nombrados
    def imprime_user(nombre="Arturo", apellido="Cabrera"):
        print(f"El nombre del cliente es {nombre} {apellido}")


    imprime_user(apellido="Guerrero", nombre="Brunilde")

# xargs es poder pasarle N argumentos a la funcion
    def suma(*numeros):
        result = 0
        for numero in numeros:
            result += numero
        print(result)


    suma(2, 5)
    suma(3, 4, 3)

# kwargs
    ## es obligatorio el nombre del parametro cuando se trabaje con kwargs
    def get_product(**datos):
        print(datos)


    get_product(id="id", name="shoes", sku="nike001")

    ## acceder a los parametros en la funcion
    def get_product(**datos):
        print(datos["id"], datos["name"])


    get_product(id="01", name="shoes", sku="nike001")


# modulos
    # cada uno de los archivos .py que generamos en python se denominan modulos, y son considerados contenedores para organizar nuestro codigo

    #paquetes
    # un pauqete es un modulo que sirve para contener otros modulos y paquetes, en la practica es un directorio que contiene un archivo '__init__.py
    # dentro de dicho directorio podremos tener almacenados otros modulos o paquetes
    # .
    # |-- modulo1.py
    # |-- paquete
    #   |-- __init__.py
    #   |-- modulo1.py
    #   |-- subpaquete
    #       |-- __init__.py
    #       |-- modulo1.py
    #       |-- modulo2.py


    import math
    help(math) # mostrar la descripcion de la libreria
    print(math.cos(math.pi))  #coseno de pi

    # funciones desde objetos
    miTexto = "el perro de san roque no tiene rabo"
    help(str)
    str.title(miTexto)  #poner el principio de cada palabra en mayuscula
    miTexto.title()     # lo mismo que en lo anterior
    miTexto.replace('san','mr')  #replazar palabras
    miTexto.replace('san','mr').title()


# CADENAS DE TEXTOS
    refran = "el perro de san roque no tiene rabo "
    refran = refran + 'porque ramon rodriguez se lo ha robado'
    print(refran)
    print(refran*2)  # lo repite * cuantas veces se le indique

    ## la \ nos ayuda a organizarnos
    refran = "el perro de san roque no tiene rabo "\
            "porque ramon rodriguez se lo ha robado, "\
            "esto es un refran tipico de España."
    print(refran)

    ## la \n es el salto de linea
    refran = "el perro de san roque no tiene rabo \n"\
            "porque ramon rodriguez se lo ha robado, \n"\
            "esto es un refran tipico de España."
    print(refran)

    ## el ''' para escribir enb varias lineas e interprete saltos de lineas y espacios
    refran = '''el perro de san roque no tiene rabo 
            porque ramon rodriguez se lo ha robado, 
            esto es un refran tipico de España. ole toro'''
    print(refran)


    # contar el tamaño de la cadena
    refran = 'El perro de San Roque no tiene rabo ...'
    print(len(refran))  # contar la cadena
    print(refran[0])    #posicion 0
    print(refran[38])   #posicion final
    print(refran[3:21]) #principio - fin
    print(refran[:21])  # desde el inicio hasta la posicion indicada de final
    print(refran[21:])  # desde la posicion 21 hasta el final de la cadena
    print(refran[:-10]) # desde el principio hasta -10 posisciones del final
    print(refran[-10:]) # los 10 ultimos caracteres

# FUNCIONES MAS USADAS CON CADENAS DE CARACTERES
    print(refran.upper())
    refran.lower()                  #todas a minusculas
    refran.upper()                  #todas a mayusculas
    refran.capitalize()             #la primera letra de la cadena
    str.title(refran)               # poner el principio de cada palabra en mayuscula
    refran.title()                  # lo mismo que en lo anterior
    refran.replace('no', 'si')      #remplazar todo del primer parametro por l segundo
    refran.find('Roque')            #busca una palabra o un caracter e indica en que posicion esta
    refran.find('roque')            #-1 si no la encuentra, distingue mayuscula de minuscula
    print("rabo" in refran)         # busca si existe
    print("rabo" not in refran)     # busca si no existe
    refran.lower().find('roque')    #pasar a minuscula y buscar la palabra o letra
    refran.strip()                  #elimina los espacios del rpincio y del final
    refran.rstrip()                 # elimina los espacios de la derecha
    refran.lstrip()                 # elimina los espacios de la izquierda
    refran.split()                  #crea uan lista con cada elemento de la cadena de texto
    refran.split('no')              #parte la cadena en las veces que exista esa palabra o letra, quitando la palabra o letra que se pase por parametro
    refran.isupper()                #para determinar si una letra está en mayúscula
    refran.islower()                #para determinar si una letra está en minuscula

    test = "1--2--3--4--5"
    # split() puede seleccionar la posición en una cadena desde el frente para dividir.
    print(test.split("--", 2))
    # rsplit() puede seleccionar la posición en una cadena desde atrás para dividir.
    print(test.rsplit("--", 2))
    # salida
    ['1', '2', '3--4--5']  # split()
    ['1--2--3', '4', '5']  # rsplit()

# FORMATEANDO CADENAS
    cadena = " esto es una cadena con espacios "
    print(cadena)
    print(cadena.capitalize())
    print(cadena.strip().capitalize())

    ## EJERCICIOS:
    ### como podemos extraer la palabra "casa" de la siguiente cadena: "Tengo una casa roja" guardada en la variable frase?
    frase = "Tengo una casa roja"
    print(frase[frase.find('casa'):frase.find('casa')+len('casa')])

# CONDICIONALES
    ## if
    EDAD = 18
    edad_votante = int(input("Ingrese su edad: "))
    if edad_votante < EDAD:
        print("No tiene edad para Votar")
    if edad_votante >= EDAD:
        print("Felicidades Puede votar")


    ## else
    edad_votante = int(input("Ingrese su edad: "))
    if edad_votante < EDAD:
        print("No tiene edad para Votar")
    else:
        print("Felicidades Puede votar")

    ## elif
    ### es importante que en caso de enteros, se debe evaluar de mayor a menor
    edad_cinefilo = int(input("Ingrese su edad cinefilo: "))
    if edad_cinefilo > 54:
        print("Puede ver la pelicula con descuento")
    elif edad_cinefilo > 17:
        print("Puedes ver la pelicula")
    else:
        print("No puedes entrar")
        print("Ve a otro lado")

    print("Listo")


    ## ternario
    edad_cinefilo = int(input("Ingrese su edad cinefilo: "))
    mensaje = "Puede ver la pelicula" if edad_cinefilo > 18 else "no puedes entrar"
    print(mensaje)

# OPERADORES LOGICOS
    # and, or, not
    gas = False
    encendido = True
    edad = 18

    if gas and encendido and edad > 17:
        print("Puedes avanzar")

    if gas or encendido:
        print("Puedes avanzar ve")

    if not gas and (encendido and edad > 17):
        print("No Puedes avanzar sin gas")

    ## tambien se puede hacer de la siguiente manera
    edad = 25
    if 15 <= edad <= 65:
        print("puede entrar a la piscina")

# LISTAS
numeros = [1, 2, 3, 4, 5,]
print(numeros)          # imprime la lista completa
print(numeros[1])       # imprime lo que esta en esa pocion que le pasemos

## lista de string
letras = ["a", "e", "i", "o", "u"]
print(letras)

palabras = ["algo", "esta", "interesante", "oculto", "universidad"]
print(palabras)

## lista de booleans
booleans = [True, False, True, False]
print(booleans)

## lista de listas
matriz = [[1, 1], [1, 0]]
print(matriz)

## unir listas
alfanumericos = numeros + letras
print(alfanumericos)

## range y list
lista = list(range(1, 4))
print(lista)

chars = list("aprendiendo con gnuxdar")
print(chars)

# MANIPULANDO LISTAS
users = ["gnuxdar", "admin", "newbie", "jedi"]
print(users)

users[3] = "yoda"
print(users)
print(users[1:])    # desde la posicion 1 hasta el ultimo
print(users[-1])    # con negativos (-) va desde el ultimo al primero de la lista, -1, -3, -N
print(users[::2])   # imprime los pares, comeinza desde el inicio y va a (dos) despues: ['gnuxdar', 'newbie']
print(users[1::2])  # immprime desde la posicion 1 (el segundo) y luego a cada dos:

numeros = list(range(21))
print(numeros[::2])     # imprime los numero pares de esa list
print(numeros[1::2])    # imprime los numero impares de esa list (inicio::cada tantos numeros)

# DESEMPAQUETAR LISTAS
numeros = [1, 2, 3]

# manera incorrecta!
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]
# print(primero, segundo, tercero)

primero, segundo, tercero = numeros
# aca se le asigna dinamicamente a cada variable un valor de una posicion
print(primero, segundo, tercero)
print(segundo)                      # podemos acceder al valor de la variable

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# despues de declarar una variable despues de *otros, esta reseva el valor de N variables que se asignen, cada variable es un valor de la lista
primero, *otros, ultimo = numeros
print(primero, ultimo, otros)

# iterar listas
mascotas = ["zeus", "thitan", "sky"]

for mascota in enumerate(mascotas):
    # Devuelve un objeto de enumeración. iterable debe ser una secuencia, un iterador o algún otro objeto que soporte la iteración.
    # El método __next__() del iterador devuelto por enumerate() devuelve una tupla que contiene un recuento
    # (desde el inicio, que por defecto es 0) y los valores obtenidos al iterar sobre iterable.
    print(mascota)
    # print(mascota[0])  # [0] la posicion de la lista, [1] el valor de la lista

# acceder a los indices de una lista
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)

# buscar el indice de elementos en una lista
mascotas = ["zeus", "titan", "sky", "titan"]
# index() muestra el indice del elemento en la lista
print(mascotas.index("titan"))

# contar elementos de una lista
mascotas = ["zeus", "titan", "sky", "titan"]
# count() cuenta, cuantos de esos elementos en la lista hay
print(mascotas.count("titan"))

if "titan" in mascotas:  # valida si existe en al lista
    print(mascotas.index("titan"))

# agregando y eliminando elementos de una lista
mascotas = ["zeus", "titan", "sky", "titan"]
# Inserte un nuevo elemento con valor x en la matriz antes de la posición i. Los valores negativos se tratan como relativos al final de la matriz.
mascotas.insert(2, "downie")
mascotas.append("beta")         # inserta un elemento al final de la lista
mascotas.remove("titan")        # elimina la primera coincidencia que exista
mascotas.pop()                  # elimina el ultimo elemento de la lista
# elimina el elemento de la lista, que este en el indice que le pasemos
mascotas.pop(2)
# parecido al anterior, pero influye directamente en la posicion o indice
del mascotas[1]
mascotas.clear()                # como su nombre lo indica, limpia por completo la lista
print(mascotas)

# ordenando listas
numeros = [10, 23, 50, 5, 12, 30]
# numeros.sort()  # ordena la lista
# numeros.sort(reverse=True)  # ordena la lista de forma descendente
numeros2 = sorted(numeros)  # crea una copia nueva lista
# tambien podemos ordenarla alreves de la misma manera que antes
numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

# ordenando listas de listas
# siempre y cuando el primer valor de las sublistas sean numeros
users = [
    [1, "admin"],
    [7, "gnuxdar"],
    [5, "grebo"]
]
users.sort()
print(users)

# otro metodo para ordenar
users = [
    ["admin", 1],
    ["gnuxdar", 7],
    ["grebo", 5]
]
users.sort(key=lambda el: el[1], reverse=True)  # reverse=True es opcional
print(users)

# listas de comprension
users = [
    ["admin", 1],
    ["gnuxdar", 7],
    ["grebo", 5]
]

# crear un listado de nombres
names = []
for user in users:
    names.append(user[0])
print(names)

# forma mas corta de hacerlo
# names = [expresion for item in items]
names = [user[0] for user in users]
# names = [name[0] for name in names]   # imprimir la primera letra de cada item
print(names)

# listas con map() y filter()
    # map() para tranformar a los usuarios

    users = [
        ["admin", 1],
        ["gnuxdar", 7],
        ["grebo", 5]
    ]

    names = list(map(lambda user: user[0], users))
    print(names)

    # filter()
    menos_users = list(filter(lambda user: user[1] > 2, users))
    print(menos_users)

# sets: grupo o conjunto
    primer = {1, 1, 1, 9, 1, 2, 2, 3, 3, 6}
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

# tuplas, son como las listas, pero estas no se pueden editar
    users = ("Arturo", "gnuxdar")
    print(users)

    odd_numbers = (1, 3, 5, 7, 9)
    pair_numbers = (2, 4, 6, 8)
    print(odd_numbers + pair_numbers)

    # como convertir una lista a una tupla
    lista = [1, 2]
    print(type(lista))

    converter = tuple(lista)
    print(type(converter))

    # en las tuplas se puedehacer todo lo que se hace con una lista, pero que no edite o elimine
    menosNumeros = odd_numbers[:2]
    print(menosNumeros)
    primero, segundo, *otros = odd_numbers
    print(primero, segundo, otros)
    for n in odd_numbers:
        print(n)

    # en tal caso de editar una tupla, esta se tendra que pasar a list, en realidad, se crea una list en base de la tupla
    lista_numeros = list(odd_numbers)
    lista_numeros[0] = "uno"
    print(type(lista_numeros), lista_numeros)

# diccinarios: Una matriz asociativa, donde las claves arbitrarias se asignan a valores.
    # Las claves pueden ser cualquier objeto con los métodos __hash__() y __eq__(). Llamado hash en Perl
    user = {
        "id": 2,
        "name": "Arturo",
        "lastname": "Cabrera",
        "nickname": "gnuxdar"
    }

    print(user)
    print(user["name"])

    # agregar
    user["age"] = 33
    print(user)

    # como acceder a un elemento y que muestre None si no existe
    print(user.get("nickname"))
    print(user.get("idiota"))                   # None, si no existe
    # mostrar un valor por defecto si loq ue se busca no existe
    print(user.get("idiota", "no eres tu"))

    # eliminar
    del user["lastname"]
    print(user)

    del (user["age"])
    print(user)

    # iterar un diccionario
    for value in user:
        print(value, user[value])

    # una mejor manera de acceder a los itms de un diccionario
    for value in user.items():
        print(value)    # devuelve tuplas del, donde en cada una ess llave valor

    for key, value in user.items():
        print(key, value)

    # lista de diccionarios
    users = [
        {"id": 5, "name": "Arturo"},
        {"id": 6, "name": "Jose"},
        {"id": 7, "name": "Alexa"},
        {"id": 8, "name": "Rosa"},

    ]

    for value in users:
        print(value["name"])
