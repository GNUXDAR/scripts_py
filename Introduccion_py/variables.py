# variables y una lista de palabras reservada que python declara
help('keywords')

first_name = 'Arturo'
last_name = 'Cabrera'
country = 'Venezuela - Ecuador'
city = 'Quito'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'PHP', 'Python']
person_info = {
    'firstname': 'Arturo',
    'lastname': 'Cabrera',
    'country': 'Ecuador',
    'city': 'Quito'
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)


# Printing out types
print(type('Arturo'))     # str
print(type(first_name))     # str
print(type(10))             # int
print(type(3.14))           # float
print(type(1 + 1j))         # complex
print(type(True))           # bool
print(type([1, 2, 3, 4]))     # list
print(type({'name':'Arturo','age':250, 'is_married':250}))    # dict
print(type((1,2)))                                              # tuple
print(type(zip([1,2],[3,4])))                                   # set

address: str = 'Mi calle es Calceta'
print(type(address))

# Encuentre la longitud del texto python y convierta el valor en flotante y conviértalo en una cadena
long_python = len('python')
print(type(str(float(long_python))))

# multiple asignacion de variables en una solo linea (mala practica)
name, lastname, nickname, age = 'Arturo', 'Cabrera', 'gnuxdar', 33
print('My nombre es ',name, lastname, 'me consigues en las redes como: ', nickname, 'y tengo ', age, 'años de edad')
