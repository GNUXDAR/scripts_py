# and, or, not
gas =  False
encendido = True
edad = 18

if gas and encendido and edad > 17:
    print("Puedes avanzar")

if gas or encendido:
    print("Puedes avanzar ve")

if not gas and (encendido and edad > 17):
    print("No Puedes avanzar sin gas")
    
## tambien se puede hacer de la siguiente manera
edad = 25
if 15 <= edad <= 65:
    print("puede entrar a la piscina")
