# La vida está llena de rutinas. En programación también hacemos muchas tareas repetitivas.
# Para manejar tareas repetitivas, los lenguajes de programación usan bucles.
# El lenguaje de programación Python también proporciona los siguientes tipos de dos bucles: for, while

# Usamos la palabra reservada while para hacer un bucle while. Se utiliza para ejecutar un bloque de declaraciones repetidamente hasta que se cumpla una condición dada. 
# Cuando la condición se vuelve falsa, las líneas de código después del ciclo continuarán ejecutándose.

numero = 1
while numero < 100:
    print(numero)
    numero *= 2

comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

# while infinito
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "exit":
        break

# while -c continue
count = 0
while count < 5:
    if count == 3:
        continue
    print(count)
    count = count + 1
    
# while - else
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
# 0 1 2 3 4 5
