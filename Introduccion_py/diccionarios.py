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