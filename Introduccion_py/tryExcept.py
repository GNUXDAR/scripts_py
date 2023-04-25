# try:
#     código en este bloque si las cosas van bien
# except:
#     el código en este bloque se ejecuta si las cosas van mal

# ejemplo
try:
    print(10 + '5')
except:
    print('Something went wrong')  # Algo salió mal

# cuando no sabemos bien cual es el error
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except:
    print('Something went wrong')
# Something went wrong
# En el ejemplo anterior, el bloque de excepción se ejecutará y no conocemos exactamente el problema. 
# Para analizar el problema, podemos usar los diferentes tipos de error con excepción.

# En el siguiente ejemplo, manejará el error y también nos dirá el tipo de error generado.
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
# Enter your name:Arturo
# Year you born: 1989
# Type error occured

# En el código anterior, la salida será TypeError. Ahora, agreguemos un bloque adicional:
try:
    name = input('Introduzca su nombre:')
    year_born = input('Año que naciste:')
    age = 2019 - int(year_born)
    print(f'Tu nombre es {name}. Y tu edad es {age}.')
except TypeError:
    print('Se produce un error de tipo')
except ValueError:
    print('Se produce un error de valor')
except ZeroDivisionError:
    print('se produce un error de división por cero')
else:
    print('Usualmente corro con el bloque try')
finally:
    print('Siempre corro.')

# También se acorta el código anterior de la siguiente manera:
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except Exception as e:
    print(e)

# EMPAQUETAR Y DESEMPAQUETAR ARGUMENTOS EN PYTHON 
# Usamos dos operadores:
# * para tuples
# ** para dictionaries
# Permítenos tomar el siguiente ejemplo. Este toma solo argumentos, pero tenemos una lista. Podemos desempaquetar la lista y cambiarla a argumentos.

# DESEMPAQUETAR
# Desempaquetando listas
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
# Cuando ejecutamos este código, genera un error, porque esta función toma números (no una lista) como argumentos. 
# Descomprimamos/desestructuramos la lista.


def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
# También podemos usar el desempaquetado en la función incorporada de rango que espera un comienzo y un final.

numbers = range(2, 7)  # llamada normal con argumentos separados
print(list(numbers))  # [2, 3, 4, 5, 6]
args = [2, 7]
numbers = range(*args)  # llamar con argumentos desempaquetados de una lista (no funciona)
print(numbers)      # [2, 3, 4, 5,6]

# Una lista o una tupla también se pueden descomprimir así:
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)  # 1 [2, 3, 4, 5, 6] 7



try:
  valor = input('Escribe el número: ') #pero el usuario lo pone con letras
  valorNumerico = int(valor)
  resultado = valorNumerico + 3
  print(resultado)
except Exception as e:
    print('Hemos sufrido un error debido a que: ',str(e))


# tipos de errores
try:
  valor = input('Introduce un valor: ') 
  valorNumerico = int(valor) #/0 #/dos
  resultado = 0 / valorNumerico 
  print(resultado)
except ArithmeticError:
  print('Error aritmético')
except ValueError:
    valorNumerico = 0
except Exception as e:
   print('Hemos subrido un error debido a que:',str(e))

print(valorNumerico + 3)

# Escribe una función llamada check-season, toma un parámetro de mes y devuelve la estación: Otoño, Invierno, Primavera o Verano.
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

"""
En Python, raise se utiliza para generar una excepción específica en un bloque de código. 
Cuando se utiliza raise en un bloque try-except, se puede especificar el tipo de excepción que se va a generar 
y opcionalmente se puede proporcionar un mensaje detallado para indicar la causa de la excepción.
"""
