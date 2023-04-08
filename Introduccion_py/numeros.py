import math
numero = 5      # entero -> integer
decimal = 1.2   # float

suma = 10 + 8 
resta = 18 - 8 
multiplicar = 16*2  
dividir = 10 / 2
divicion_sin_decimal = 1 // 3
modulo = 1 % 3
potencia = 2 ** 3

# otra notacion
## numero += 5
## numero -= 3
## numero *= 5
## numero /= 2
numero //= 2


print(dividir)
print(divicion_sin_decimal)
print(modulo)
print(potencia)
print(f"numero  {numero}")

# Funciones matematicas
## round()  #Devuelve el número redondeado a la precisión de los dígitos después del punto decimal. Si se omite ndigits o es None, devuelve el entero más cercano a su entrada.
print(round(1.3))
print(round(1.5))
print(round(1.7))
## abs() Devuelve el valor absoluto de un número. El argumento puede ser un número entero, un número de coma flotante o un objeto que implemente __abs__(). Si el argumento es un número complejo, se devuelve su magnitud.
print(abs(-44))
print(abs(44))

# Comparadores logicos
print(1 < 2)
print(1 > 2)
print(1 <= 2)
print(1 >= 2)
print(1 == 2)
print(2 == "2")
print(1 != 2)
print(1 != "2")

# Modulos
# Devuelve el techo de x, el entero más pequeño mayor o igual que x. Si x no es un flotante, delega a x.__ceil__, que debería devolver un valor integral.
print(math.ceil(1.1))
# Devuelve el piso de x, el entero más grande menor o igual que x. Si x no es un flotante, delega a x.__floor__, que debería devolver un valor Integral.
print(math.floor(1.999))
# print(math.isnan("23"))         # Devuelve True si x es un NaN (no un número) y False en caso contrario.
print(math.pow(10, 3))  # potencia, base, exponente
print(math.sqrt(9))         # la raiz cuadrada del numero argumento
print(math.nextafter(10, 8))
