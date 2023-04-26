# Modos de apertura de ficheros

# | Indicador | Modo de apertura                                                                                     | Ubicación del puntero                                                        |
# |-----------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
# | r         | Solo lectura     valor predeterminado                                                                | Al inicio del archivo                                                        |
# | rb        | Solo lectura en modo binario                                                                         | Al inicio del archivo                                                        |
# | r+        | Lectura y escritura                                                                                  | Al inicio del archivo                                                        |
# | rb+       | Lectura y escritura en modo binario                                                                  | Al inicio del archivo                                                        |
# | w         | Solo escritura. Sobreescribe el archivo si existe. Crea el archivo si no existe                      | Al inicio del archivo                                                        |
# | wb        | Solo escritura en modo binario. Sobreescribe el archivo si existe. Crea el archivo si no existe      | Al inicio del archivo                                                        |
# | w+        | Escritura y lectura. Sobreescribe el archivo si existe. Crea el archivo si no existe                 | Al inicio del archivo                                                        |
# | wb+       | Escritura y lectura en modo binario. Sobreescribe el archivo si existe. Crea el archivo si no existe | Al inicio del archivo                                                        |
# | a         | Añadido (agregar contenido). Crea el archivo si éste no existe                                       | Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo |
# | ab        | Añadido en modo binario (agregar contenido). Crea el archivo si éste no existe                       | Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo |
# | a+        | Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.                            | Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo |
# | ab+       | Añadido (agregar contenido) y lectura en modo binario. Crea el archivo si éste no existe             | Si el archivo existe, al final de éste. Si el archivo no existe, al comienzo |

# Hasta ahora hemos visto diferentes tipos de datos de Python. Por lo general, almacenamos nuestros datos en diferentes formatos de archivo. 
# Además del manejo de archivos, también veremos diferentes formatos de archivo (.txt, .json, .xml, .csv, .tsv, .excel) en esta sección. 
# Primero, familiaricémonos con el manejo de archivos con formato de archivo común (.txt).

# El manejo de archivos es una parte importante de la programación que nos permite crear, leer, actualizar y eliminar archivos. 
# En Python, para manejar datos, usamos la función integrada open().
# Syntax
# open('filename', mode)  # mode(r, a, w, x, t,b) podría ser leer, escribir, actualizar

# Abrir archivos para leer
# Creé y guardé un archivo llamado read_file_example.txt en el directorio de archivos. Veamos cómo se hace:
import xml.etree.ElementTree as ET
f = open('Introduccion_py/files/read_file_example.txt')
print(f)    # <_io.TextIOWrapper name='Introduccion_py/files/read_file_example.txt' mode='r' encoding='UTF-8'>
# Como puede ver en el ejemplo anterior, imprimí el archivo abierto y brindó información al respecto. 
# El archivo abierto tiene diferentes métodos de lectura: read(), readline, readlines. Un archivo abierto debe cerrarse con el método close().

# read(): lee todo el texto como una cadena. Si queremos limitar el número de caracteres que queremos leer,
# podemos limitarlo pasando el valor int al método read(number).
f = open('Introduccion_py/files/read_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()

# output
# <class 'str' >
# This is an example to show how to open a file and read.
# This is the second line of the text.

# En lugar de imprimir todo el texto, imprimamos los primeros 10 caracteres del archivo de texto.
f = open('Introduccion_py/files/read_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()

# output
# <class 'str' >
# This is an

# readline(): lee solo la primera línea
f = open('Introduccion_py/files/read_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
f.close()

# output
# <class 'str' >
# This is an example to show how to open a file and read.

# readlines(): lee todo el texto línea por línea y devuelve una lista de líneas
f = open('Introduccion_py/files/read_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()

# output
# <class 'list' >
# ['This is an example to show how to open a file and read.\n',   'This is the second line of the text.']

# Otra forma de obtener todas las líneas como una lista es usando splitlines():
f = open('Introduccion_py/files/read_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()

# output
# <class 'list'>
# ['This is an example to show how to open a file and read.', 'This is the second line of the text.']

# Después de abrir un archivo, debemos cerrarlo. Hay una alta tendencia a olvidarse de cerrarlos. 
# Hay una nueva forma de abrir archivos usando with - cierra los archivos por sí mismo. 
# Reescribamos el ejemplo anterior con el método with:
with open('Introduccion_py/files/read_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)

# output
# <class 'list'>
# ['This is an example to show how to open a file and read.', 'This is the second line of the text.']

# Abrir archivos para escribir y actualizar
# Para escribir en un archivo existente, debemos agregar un modo como parámetro a la función open(): 
#   "a" - agregar - se agregará al final del archivo, si el archivo no lo hace, crea un nuevo archivo. 
#   "w" - escribir - sobrescribirá cualquier contenido existente, si el archivo no existe, lo crea.
# Agreguemos algo de texto al archivo que hemos estado leyendo:
with open('Introduccion_py/files/read_file_example.txt', 'a') as f:
    f.write('This text has to be appended at the end')

# El siguiente método crea un nuevo archivo, si el archivo no existe:
with open('Introduccion_py/files/read_file_example.txt', 'w') as f:
    f.write('This text will be written in a newly created file')

# Eliminación de archivos
# Hemos visto en la sección anterior cómo crear y eliminar un directorio usando el módulo os. 
# Nuevamente ahora, si queremos eliminar un archivo, usamos el módulo os.
import os
os.remove('Introduccion_py/files/example.txt')

# Si el archivo no existe, el método de eliminación generará un error, por lo que es bueno usar una condición como esta:
import os
if os.path.exists('Introduccion_py/files/example.txt'):
    os.remove('Introduccion_py/files/example.txt')
else:
    print('The file does not exist')

#  TIPOS DE ARCHIVOS
# Archivo con extensión txt
# El archivo con extensión txt es una forma de datos muy común y lo hemos cubierto en la sección anterior. Pasemos al archivo JSON.
# Archivo con extensión json
# JSON significa Notación de objetos de JavaScript. En realidad, es un objeto de JavaScript en forma de cadena o un diccionario de Python.

# dictionary
person_dct = {
    "name": "Arturo",
    "country": "Venezuela",
    "city": "Tunapuy",
    "skills": ["JavaScrip", "React", "Python"]
}
# JSON: Una cadena forma un diccionario
person_json = "{'name': 'Arturo', 'country': 'Venezuela', 'city': 'Tunapuy', 'skills': ['JavaScrip', 'React', 'Python']}"

# usamos tres comillas y las hacemos de varias líneas para que sea más legible
person_json = '''{
    "name":"Arturo",
    "country":"Venezuela",
    "city":"Tunapuy",
    "skills":["JavaScrip", "React","Python"]
}'''

# Cambiando JSON a Diccionario
# Para cambiar un JSON a un diccionario, primero importamos el módulo json y luego usamos el método de carga.
import json
# JSON
person_json = '''{
    "name": "Arturo",
    "country": "Venezuela",
    "city": "Tunapuy",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# cambiemos JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

# cambiando diccionario a JSON
# Para cambiar un diccionario a JSON, usamos el método dumps del módulo json
import json
# python dictionary
person = {
    "name": "Arturo",
    "country": "Venezuela",
    "city": "Tunapuy",
    "skills": ["JavaScrip", "React", "Python"]
}
# vamos a convertirlo a json
person_json = json.dumps(person, indent=4)  # sangría podría ser 2, 4, 8. Embellece el json
print(type(person_json))
print(person_json)

# GUARDANDO UN ARCHIVO JSON 
# También podemos guardar nuestros datos como un archivo json. Guardémoslo como un archivo json siguiendo los siguientes pasos. 
# Para escribir un archivo json, usamos el método json.dump(), puede tomar diccionario, archivo de salida, sure_ascii y sangría.
import json
# python dictionary
person = {
    "name": "Arturo",
    "country": "Venezuela",
    "city": "Tunapuy",
    "skills": ["JavaScript", "React", "Python", "PHP"]
}
with open('Introduccion_py/files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
# En el código anterior, usamos codificación y sangría. La sangría hace que el archivo json sea fácil de leer.

# Archivo con extensión csv
# CSV significa valores separados por comas. CSV es un formato de archivo simple que se utiliza para almacenar datos tabulares, 
# como una hoja de cálculo o una base de datos. CSV es un formato de datos muy común en la ciencia de datos.
# example
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"

import csv
with open('Introduccion_py/files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a studen. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

# Archivo con extensión xlsx
# Para leer archivos de Excel necesitamos instalar el paquete xlrd. Cubriremos esto después de que cubramos la instalación del paquete usando pip.
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)

# Archivo con extensión xml
# XML es otro formato de datos estructurados que se parece a HTML. En XML, las etiquetas no están predefinidas. 
# La primera línea es una declaración XML. La etiqueta de person es la raíz del XML. La person tiene un atributo de género. Ejemplo:XML
<?xml version="1.0"?>
<person gender="female">
    <name>Arturo</name>
    <country>Venezuela</country>
    <city>Tunapuy</city>
    <skills>
        <skill>PHP</skill>
        <skill>React</skill>
        <skill>Python</skill>
    </skills>
</person>
# para mas informacion en como leer un XML, revisa la documentacion: https://docs.python.org/2/library/xml.etree.elementtree.html
tree = ET.parse('Introduccion_py/files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)

# output
# Root tag: person
# Attribute: {'gender': 'male'}
# field: name
# field: country
# field: city
# field: skills
