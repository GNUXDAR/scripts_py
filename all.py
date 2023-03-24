# mostrar mensaje por pantalla
print ("Hola Mundo");

# capturar valores por pantalla (input) y mostrar
nombre = input('escribe tu nombre ')
print(nombre)

# como saber si un anio es bisiesto
print ("Digite el año:")
anio = int(input()) #convertir en entero

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print ("Año bisiesto")

else:
    print ("Año NO bisiesto")

# mostrar si el numero ingresao es pas o impar
num = input('Introduce un número:')
numInt = int(num)
if (numInt%2==0):
    print('El numero es par')
else:
    print('El numero es impar')

# mostrar una lista
lista = list(range(1,4))
print(lista)

