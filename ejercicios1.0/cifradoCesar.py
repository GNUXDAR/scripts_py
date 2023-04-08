## podemos utilizar esta forma de almacenar los caracteres para encriptar un mensaje de forma sencilla con una encriptacion por deplazamiento
## tambien conocida como cifrado cesar
# print(ord(letra))   #codigo ASCII
# print(chr(43))      #convierte de codigo a caracter

# Cifrado
def cifrado():
    cadena=input("$>")
    cadenaCodificada=""
    desplazamiento=input("num desplazamiento:")
    desplazamiento = int(desplazamiento)
    for letra in cadena:
        cadenaCodificada = cadenaCodificada+chr(ord(letra)+desplazamiento)
    print(cadenaCodificada)

cifrado()