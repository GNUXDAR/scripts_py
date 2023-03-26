## podemos utilizar esta forma de almacenar los caracteres para encriptar un mensaje de forma sencilla con una encriptacion por deplazamiento
## tambien conocida como cifrado cesar
cadena="Sigueme en mis redes con el usuario gnuxdar"
cadenaCodificada=""
desplazamiento=7
for letra in cadena:
    cadenaCodificada = cadenaCodificada+chr(ord(letra)+desplazamiento)
cadenaDeCodificada=''
for letra in cadenaCodificada:
    cadenaDeCodificada=cadenaDeCodificada+chr(ord(letra)-desplazamiento)

print(cadena)
print(cadenaCodificada)
print(cadenaDeCodificada)