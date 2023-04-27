# 00. Declare una función add_two_numbers. Toma dos parámetros y devuelve una suma.
def add_two_numbers(param1, param2):
    """ funciona que devuelve 
    el resultado de una suma"""
    result = param1 + param2
    print(result)


add_two_numbers(3, 7)

# 01. Escriba una función llamada add_all_nums que tome un número arbitrario de argumentos y los sume todos.
# Compruebe si todos los elementos de la lista son tipos de números. Si no, dé una respuesta razonable
def add_all_nums(*xargs):
    """ suma todos los numeros que se le pase por argumentos"""
    result = 0
    for n in xargs:
        result += n
    print(result)


add_all_nums(5, 5, 5, 3, 2)

# 02. La temperatura en °C se puede convertir a °F usando esta fórmula: °F = (°C x 9/5) + 32. Escribe una función que convierta °C a °F, 
# convert_celsius_to-fahrenheit.

def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)


convert_celsius_to_fahrenheit(23)

# 03. Escribe una función llamada check-season, toma un parámetro de mes y devuelve la estación: Otoño, Invierno, Primavera o Verano.
def check_season(month):
    # abril, mayo y junio -> primavera
    # julio, agosto y septiembre. -> verano
    # octubre, noviembre y diciembre. -> otoño
    # enero, febrero y marzo. -> invierno
    month = month.lower()
    try:
        if month == 'abril' or month == 'mayo' or month == 'junio':
            print('Primavera')
        elif month == 'julio' or month == 'agosto' or month == 'septiembre':
            print('verano')
        elif month == 'octubre' or month == 'noviembre' or month == 'diciembre':
            print('otoño')
        elif month == 'enero' or month == 'febreo' or month == 'marzo':
            print('invierno')
        else:
            raise ValueError('Mes no valido')
    except ValueError as error:
        print(error)
        # print('Le invito a que revise bien lo que ingreso', month)


check_season('abril')

# 04. Declare una función llamada print_list. Toma una lista como parámetro e imprime cada elemento de la lista.
def print_list(list):
    for i in list:
        print(i)


my_list = ['html5', 'css3', 'php', 'django']
print(print_list(my_list))

# 05. Declare una función llamada lista_inversa. Toma una matriz como parámetro y devuelve el reverso de la matriz (uso de bucles).
def reverse_list(my_list):
    new_list = list()
    for i in my_list:
        new_list.insert(0, i)
    print(new_list)


my_list = ['html5', 'css3', 'php', 'django']
reverse_list(my_list)    # ['django', 'php', 'css3', 'html5']

