import hashlib
import base64
"""
Este código utiliza el algoritmo de cifrado XOR para encriptar los datos del archivo. 
La contraseña se convierte en un hash utilizando el algoritmo de hash SHA-256, 
y luego se realiza una operación XOR byte a byte entre los datos del archivo y el hash de la contraseña para encriptarlos. 
Los datos encriptados se codifican en base64 antes de escribirlos en el nuevo archivo.
"""

def encriptar_archivo(archivo, contraseña):
    # Calcular el hash de la contraseña
    hash_contraseña = hashlib.sha256(contraseña.encode()).digest()

    # Leer el contenido del archivo
    with open(archivo, 'rb') as file:
        data = file.read()

    # Encriptar los datos utilizando el hash de la contraseña
    datos_encriptados = bytearray()
    for i in range(len(data)):
        byte_encriptado = data[i] ^ hash_contraseña[i % len(hash_contraseña)]
        datos_encriptados.append(byte_encriptado)

    # Codificar los datos en base64
    datos_codificados = base64.b64encode(datos_encriptados)

    # Escribir los datos encriptados en un nuevo archivo
    with open('archivo_encriptado.txt', 'wb') as file:
        file.write(datos_codificados)


def desencriptar_archivo(archivo_encriptado, contraseña):
    # Calcular el hash de la contraseña
    hash_contraseña = hashlib.sha256(contraseña.encode()).digest()

    # Leer el contenido del archivo encriptado
    with open(archivo_encriptado, 'rb') as file:
        datos_codificados = file.read()

    # Decodificar los datos en base64
    datos_encriptados = base64.b64decode(datos_codificados)

    # Desencriptar los datos utilizando el hash de la contraseña
    datos_desencriptados = bytearray()
    for i in range(len(datos_encriptados)):
        byte_desencriptado = datos_encriptados[i] ^ hash_contraseña[i % len(
            hash_contraseña)]
        datos_desencriptados.append(byte_desencriptado)

    # Escribir los datos desencriptados en un nuevo archivo
    with open('archivo_desencriptado.txt', 'wb') as file:
        file.write(datos_desencriptados)



# Ejemplo de uso
encriptar_archivo('encripted.txt', 'gnuxdar123')

# Ejemplo de uso
desencriptar_archivo('archivo_encriptado.txt', 'gnuxdar123')
