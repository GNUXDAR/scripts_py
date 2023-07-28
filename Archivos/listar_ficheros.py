import os

def listar_archivos_en_directorio(directorio, archivo_salida):
    # Obtener una lista de los nombres de los ficheros en el directorio
    nombres_ficheros = os.listdir(directorio)

    # Escribir los nombres de los ficheros en el archivo de salida
    with open(archivo_salida, 'w') as archivo:
        for nombre_fichero in nombres_ficheros:
            archivo.write('php artisan migrate --path=/database/migrations/tenant/' + nombre_fichero + '\n') 
            # automatizar y listar migraciones de laravel

# Directorio que quieres analizar
directorio_a_listar = '/var/www/html/lv_project/database/migrations/tenant/' #'/ruta/del/directorio'

# Nombre del archivo de salida donde se guardarán los nombres de los ficheros
archivo_salida = 'nombres_ficheros.txt'

# Llamar a la función para listar los ficheros en el directorio y escribirlos en el archivo de salida
listar_archivos_en_directorio(directorio_a_listar, archivo_salida)
