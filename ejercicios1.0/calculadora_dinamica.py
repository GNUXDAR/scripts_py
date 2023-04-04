# crear una calculadora que solicite un numero,
# luego que solicite la operacion (suma, esta, multiplicacion o divicion)
# y luego que solicite otro numero y muestre el resultado de la operacion,
# seguido que solicite un numero y luego una operacion
# que solicite un numero y haga la operacion con el resultado de la anterior operacion

print("""
Bienvenido a la calculadora en Python
Para salir, escribir \"salir\"
""")
num1 = int(input("Ingresa un numero "))
opc = ""
resultado = 0
while opc.lower() != "salir":
    opc = input("Ingrese \"suma\" \"resta\" \"multi\" \"div\" ó \"salir\" ")
    if opc == "suma":
            num2 = int(input("Ingresa un numero "))
            resultado = num1 + num2
            print(f"El resultado es {resultado}")
            num1 = resultado
    elif opc == "resta":
        num2 = int(input("Ingresa un numero "))
        resultado = num1 - num2
        print(f"El resultado es {resultado}")
        num1 = resultado
    elif opc == "multi":
        num2 = int(input("Ingresa un numero "))
        resultado = num1 * num2
        print(f"El resultado es {resultado}")
        num1 = resultado
    elif opc == "div":
        num2 = int(input("Ingresa un numero "))
        resultado = num1 / num2
        print(f"El resultado es {resultado}")
        num1 = resultado
    else:
         print("operacion invalida")
         break
    
