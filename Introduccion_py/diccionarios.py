#diccinarios: Una matriz asociativa, donde las claves arbitrarias se asignan a valores. {clave: valor}
#Las claves pueden ser cualquier objeto con los métodos __hash__() y __eq__(). Llamado hash en Perl
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(type(dct))

user = {
    'id': 2,
    'first_name': 'Arturo',
    'last_name': 'Cabrera',
    'nick_name': 'gnuxdar',
    'country': 'LATAM',
    'is_marred': True,
    'skills': ['PHP', 'Python', 'JavaScript', 'Sql'],
    'address': {
        'street': 'Rigoberto Heredia',
        'zipcode': 173030
    }
    }
# El diccionario anterior muestra que un valor puede ser cualquier tipo de datos: cadena, booleano, lista, tupla, conjunto o un diccionario.

print(user)
print(user['first_name'])

# agregar
user['age'] = 33    # llave: valor "que no existen"
print(user)

user['skills'].append('HTML')   # se carga a la lista de  'skills': ['PHP', 'Python', 'JavaScript', 'Sql', 'HTML'],

# verificar llave en un diccionario
print('skills' in user)  # True

# modificar elemento del diccionario
user['last_name'] = 'Guerrero'  # 'last_name': 'Guerrero'

# como acceder a un elemento y que muestre None si no existe
print(user.get('nickname'))
print(user.get('idiota'))                   # None, si no existe
print(user.get('idiota', 'no eres tu'))     # mostrar un valor por defecto si loq ue se busca no existe

# eliminar
# pop(key): elimina el elemento con el nombre de la llave especificado:
# popitem(): elimina el último elemento
# del: elimina un elemento con el nombre de llave especificado
user.pop('nick_name')
user.popitem()

del user['last_name']
print(user)

# iterar un diccionario
for value in user:
    print(value, user[value])

# una mejor manera de acceder a los items de un diccionario
for value in user.items():
    print(value)    # devuelve tuplas del, donde en cada una es llave valor

for key, value in user.items():
    print(key, value)

# copiar un diccionario: Podemos copiar un diccionario usando un método copy(). Usando la copia podemos evitar la mutación del diccionario original.
copy_dct = user.copy() # un clon del diccionario

# obtener "llaves" de diccionario como una lista
keys = user.keys()  # dict_keys(['id', 'first_name', 'last_name', 'nick_name', 'country', 'is_marred', 'skills', 'address'])

# obtener "valor" de diccionario como una lista
values = user.values()  # dict_values([2, 'Arturo', 'Cabrera', 'gnuxdar', 'LATAM', True, ['PHP', 'Python', 'JavaScript', 'Sql'], {'street': 'Rigoberto Heredia', 'zipcode': 173030}])

# lista de diccionarios
users = [
    {'id': 5, 'name': 'Arturo'},
    {'id': 6, 'name': 'Jose'},
    {'id': 7, 'name': 'Alexa'},
    {'id': 8, 'name': 'Rosa'},

]

for value in users:
    print(value['name'])

# eliminar un diccionario
del user

# EMPAQUETAR DICCIONARIO
def packing_person_info(**kwargs):
    for key in kwargs:
        print("{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Arturo",
      country="Ecuador", city="Quito", age=33))

# DESEMPAQUETANDO DICCIONARIOS
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Arturo', 'country':'Ecuador', 'city':'Quito', 'age':33}
print(unpacking_person_info(**dct)) # Arturo lives in Ecuador, Quito. He is 33 years old.


# HAACER CALCULOS CON UN DICCIONARIO
monto_total = 244.75
comprar = {
    'compra1': 15,
    'compra2': 8,
    'compra3': 10,
    'compra4': 50,
    'compra5': 32.63
}
gasto = 0

# imprimir la clave
# for clave in comprar:
#     print(clave)

# imprimir el valor del dict
for clave in comprar:
    valor = comprar[clave]
    gasto += valor
    print(valor)
print(monto_total - gasto)

"""
porque valor = comprar[clave] toma el valor del diccionario?

Al utilizar comprar[clave], estás accediendo al valor asociado a la clave clave en el diccionario comprar. 
En cada iteración del bucle for, la variable clave toma el valor de una clave del diccionario, y comprar[clave] devuelve el valor correspondiente a esa clave.

En resumen, la línea valor = comprar[clave] asigna el valor correspondiente a la clave actual del diccionario a la variable valor, 
lo que te permite sumar ese valor al total de gastos (gasto += valor). De esta manera, estás recorriendo cada elemento del diccionario y acumulando el gasto total en la variable gasto.
"""