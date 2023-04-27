# LEYENDO DE URL
# A estas alturas ya está familiarizado con la forma de leer o escribir en un archivo ubicado en su máquina local.
# A veces, nos gustaría leer desde un sitio web usando url o desde una API.
# API significa interfaz de programa de aplicación. Es un medio para intercambiar datos estructurados entre servidores principalmente como datos json.
# Para abrir una conexión de red, necesitamos un paquete llamado request: permite abrir una conexión de red e implementar operaciones CRUD
# (crear, leer, actualizar y eliminar). En esta sección, cubriremos solo la lectura d que forma parte de un CRUD.
# instalamos request
# pip install requests

# Veremos los métodos get, status_code, headers, text y json en el módulo de solicitudes:
# get (): para abrir una red y obtener datos de la URL; devuelve un objeto de respuesta
# status_code: después de obtener los datos, podemos verificar el estado de la operación (éxito, error, etc.)
# headers: para comprobar los tipos de encabezado
# text: para extraer el texto del objeto de respuesta obtenido
# json: para extraer datos json Leamos un archivo txt de este sitio web, https://www.w3.org/TR/PNG/iso_8859-1.txt.

import requests  # importing the request module

url = 'https://www.gutenberg.org/files/1112/1112.txt'  # text from a website

response = requests.get(url)  # opening a network and fetching a data
print(response)
print(response.status_code)  # status code, success:200
print(response.headers)     # headers information
print(response.text)  # gives all the text from the page

# Leamos desde una API. API significa interfaz de programa de aplicación. Es un medio para intercambiar datos de estructura entre servidores, 
# principalmente datos json. Un ejemplo de una API: https://restcountries.eu/rest/v2/all. Leamos esta API usando el módulo request.

import requests
url = 'https://thronesapi.com/api/v2/Characters'        # characters api of game of trhone
# url = 'https://thronesapi.com/api/v2/Continents'      # continentes of game of trhone
# url = 'https://pokeapi.co/api/v2/ability'             # pokemon
response = requests.get(url)  # opening a network and fetching a data
print(response)  # response object
print(response.status_code)  # status code, success:200
print(response.headers)
characters = response.json()
# cortamos solo el primer país, eliminamos el corte para ver todos los países
# print(characters[:1])
print(characters)
# Usamos el método json() del objeto de respuesta, si estamos obteniendo datos JSON. Para txt, html, xml y otros formatos de archivo podemos usar text.
