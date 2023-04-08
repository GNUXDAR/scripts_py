#diccinarios: Una matriz asociativa, donde las claves arbitrarias se asignan a valores. 
#Las claves pueden ser cualquier objeto con los métodos __hash__() y __eq__(). Llamado hash en Perl
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
print(user.get("idiota", "no eres tu"))     # mostrar un valor por defecto si loq ue se busca no existe

# eliminar
del user["lastname"]
print(user)

del(user["age"])
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
