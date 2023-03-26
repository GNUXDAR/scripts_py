## podemos utilizar esta forma de almacenar los caracteres para encriptar un mensaje de forma sencilla con una encriptacion por deplazamiento
## tambien conocida como cifrado cesar
# print(ord(letra))   #codigo ASCII
# print(chr(43))      #convierte de codigo a caracter

# Descifrado
def descifrado():
    cadena=input("$>")
    desplazamiento=input("num desplazamiento:")
    desplazamiento = int(desplazamiento)
    cadenaDeCodificada=''
    for letra in cadena:
        cadenaDeCodificada=cadenaDeCodificada+chr(ord(letra)-desplazamiento)
    print(cadenaDeCodificada)

descifrado()