# fichero dedi#### modos de apertura de ficheros

# | Indicador | Modo de apertura                                                                                     | Ubicación del puntero                                                        |
# |-----------|------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
# | r         | Solo lectura                                                                                         | Al inicio del archivo                                                        |
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

# abrir archivos
fichero = 'pythonMoocCompanion-master/ejercicio.csv'
archivo = open(fichero)
contenido = archivo.read() ## ojo con los \n
print(contenido)
archivo.close()

#readline() lee cada linea
archivo = open(fichero, "r")
linea = archivo.readline().strip()
linea2 = archivo.readline()
print(linea)
print(linea2)
archivo.close()

# recorrer cada linea con readline()
archivo = open(fichero, "r")
print(linea)
print(linea2)
for linea in archivo.readlines():
    print(linea)
archivo.close()

#tell() nos indica en que posicion del archivo nos encontramos
print('\ntell()')
archivo = open(fichero, "r")
print(archivo.tell())
linea = archivo.readline() #al leer una linea, estara al final de esa linea
print(archivo.tell())
archivo.close()

#seek() nos manda a a un posicion en concreto
print('\nseek()')
archivo = open(fichero, "r")
archivo.read()
print(archivo.tell())   #al leer todo el archivo, se posicionara al final del mismo
archivo.seek(0)         # nos manda a la posicion que  le pasemos por parametro
print(archivo.tell())
archivo.close()

#write() para escribir en el archiuvo
archivo = open("prueba_escritura.extension",'w+') #a+ agregamos contenido en el que ya esta, w+ rescribe lo que esta basicamente
archivo.write('es una nueva cadena en el archivo\n')
archivo.close()

#flush() en ocasiones no se escribe con write() por problemas de memoria o lo que sea, con el flush volca lo que etsa en el buffer al archivo
archivo = open("prueba_escritura.extension",'a+')
archivo.write('cadena para flushear')
archivo.flush()
archivo.close()

#whit open: se cerrara el archivo si existe un error o si todo a hido bien, pero al salir del with se cierra el archivo
with open("prueba_escritura.extension",'r') as archivo:
    print(archivo.read())
print(archivo.read())   # esta linea falla proque ya se ha cerrado el archivo y esta linea esat fuera del with


#Ejercicio1: contar las lineas de un archivo
print('\nEJERCICIO 1')
fichero = 'pythonMoocCompanion-master/ejercicio.csv'
archivo = open(fichero, "r")
lineas = 0
for linea in archivo.readlines():
    lineas+=1
print(f'El archivo tiene {lineas} lineas')
archivo.close()

#Ejercicio2: modificar el ejercicio anterior para que nos muestre en pantalla aquellas lineas en las aparece la palabra "run"
print('\nEJERCICIO 2')
fichero = 'pythonMoocCompanion-master/ejercicio.csv'
archivo = open(fichero, "r")
lineas = 0
for linea in archivo.readlines():
    if 'run' in linea:
        print(linea.strip())
archivo.close()


#Ejercicio3: contar las lineas del nombre de un archivo que pueda ingresar un usuario por input()
print('\nEJERCICIO 3')
fichero = input('Ingrese el nombre del archivo que quiere contar las lineas: ')
archivo = open(fichero, "r")
lineas = 0
for linea in archivo.readlines():
    lineas+=1
print(f'El archivo {fichero} tiene {lineas} lineas')
archivo.close()

#Ejercicio4: Modifica el ejercicio anterior para evitar errores si el usuario escribe mal el nombre del archivo, cuando falle mostraremos un mensaje que diga, No se ha encontrado el archivo {nombrearchivo}
print('\nEJERCICIO 4')
try:
    fichero = input('Ingrese el nombre del archivo que quiere contar las lineas: ')
    archivo = open(fichero, "r")
    lineas = 0
    for linea in archivo.readlines():
        lineas+=1
    print(f'El archivo {fichero} tiene {lineas} lineas')
    archivo.close()
except:
    print(f'No se ha encontrado el archivo {fichero}')

# CODIGO DE CARACTERES DE FICHEROS
# definimos una función que cargue todos los párrafos y seleccione uno 
def parrafo(numerodeparrafo):
    #primero cargamos el fichero
    archivo = 'pythonMoocProblems-master/moocSemana7/Ejercicio7.1/quijote.txt'
    fichero = open(archivo)
    #lo leemos
    texto = fichero.read()
    #y seleccionamos el párrafo indicado en el parámetro 
    parrafos = texto.split('\n')
    while '' in parrafos: 
        parrafos.remove('')    
    parrafoseleccionado=parrafos[numerodeparrafo]
   
    #recordar cerrar el fichero si no se ha abierto con un with
    fichero.close()    
    print(parrafoseleccionado)

parrafo(8)

#en el caso de que el fichero se abra en un Os con otra codificacion como ANSI de windows
#es preferible pasarle la codificacion
def parrafo(numerodeparrafo):
    #primero cargamos el fichero
    archivo = 'pythonMoocProblems-master/moocSemana7/Ejercicio7.1/quijote.txt'
    # fichero = open(archivo, "r", encoding="utf-8")
    fichero = open(archivo, "r", encoding="ansi")
    #fichero = open('quijoteansi.txt', "r", encoding="ansi")
    # fichero = open('quijoteansi.txt', "r", encoding="utf-8")
    
    #lo leemos
    texto = fichero.read()
    #y seleccionamos el párrafo indicado en el parámetro 
    parrafos = texto.split('\n')
    while '' in parrafos: 
        parrafos.remove('')    
    
    parrafoseleccionado=parrafos[numerodeparrafo]
     
    #acordaos de cerrar el fichero si no lo habéis abierto con un with
    fichero.close()    
    print(parrafoseleccionado)
parrafo(8)

