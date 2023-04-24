
"""fichero de prueba"""
# convertir caractee a codigo ascii y a binario
# https://elcodigoascii.com.ar/

# Codigo de caracteres ASCII
# letra = "a"
# print(ord(letra))
# print(chr(43))
# bromecina para la gripe

########

# # 10. Esta es una lista de frutas, ['plátano', 'naranja', 'mango', 'limón'] invierta el orden usando bucle.
# fruits = ['plátano', 'naranja', 'mango', 'limón']
# new_fruits = list()
# for i in fruits:
#     new_fruits.insert(0, i)
# print(new_fruits)

###########################
# De una lista original, filtrar los elementos que no esten en la segundo lista
# user_war = ['crash', 'master pro', 'delvis', 'otto', 'el papu xd', 'lopez', 'espectrohn', 'pata de hierro', 
#             'hoffman', 'gerardo', 'computer', 'antonio', 'blasete', 'arthurx', 'billied', 'k2', 'destructor', 
#             'josegAguilera', 'mk', 'ramiro', 'gonazalito', 'andrezvnlza', 'recucus', 'renato cfc', 'andersond', 
#             'urvina', 'gastonRamos', 'Rey t Torres', 'mary', 'veloz', 'popo', 'hugo_11n', 'samugamer100', 'lopez', 
#             'alaukabar', 'zaul uwu', 'memosau', 'angel', 'idk lee', '#2']
# delete_user = ['lopez', 'espectrohn', 'gonazalito',
#                'renato cfc', 'andersond', 'urvina', 'mary', 'veloz', 'popo', 'samugamer100', 'lopez', 'zaul uwu', 'angel', '#2']

# user_war = [x for x in user_war if x not in delete_user]
# print(user_war)

# Generating numbers
# numbers = [i for i in range(11)]  # to generate numbers from 0 to 10
# print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

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
