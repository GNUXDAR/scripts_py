# if
EDAD = 18
edad_votante = int(input("Ingrese su edad: "))
if edad_votante < EDAD:
    print("No tiene edad para Votar")
if edad_votante >= EDAD:
    print("Felicidades Puede votar")


# else
edad_votante = int(input("Ingrese su edad: "))
if edad_votante < EDAD:
    print("No tiene edad para Votar")
else:
    print("Felicidades Puede votar")

# elif
## es importante que en caso de interos, se debe evaluar de mayor a menor
edad_cinefilo = int(input("Ingrese su edad cinefilo: "))
if edad_cinefilo > 54:
    print("Puede ver la pelicula con descuento")
elif edad_cinefilo > 17:
    print("Puedes ver la pelicula")
else:
    print("No puedes entrar")
    print("Ve a otro lado")

print("Listo")
