num1 = int(input("Ingresa un numero "))
num2 = int(input("Ingresa otro numero "))
suma = num1 + num2
resta = num1 - num2
multi = num1 * num2
div = num1 / num2
div_sin_decimal = num1 // num2
potencia = num1 ** num2
mensaje = f"""
Los numeros {num1} y {num2}.
Sumando da el resultado de {suma}
Resatndo da el resultado de {resta}
Multiplicando da el resultado de {multi}
Dividiendo danel resultado de {div}
Dividiendo sin decimales da el resultado de {div_sin_decimal}
Llevando a la potencia da el resultado de {potencia}
"""
print(mensaje)
