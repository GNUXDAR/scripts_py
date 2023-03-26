def conversor():
    while(True):
        print("******************************************************************************")
        print("                             CONVERSOR DE MONEDA                              ")
        print("                                 1$ = 24.40 Bs                                ")
        print("******************************************************************************")
        bolivares = input("por favor, ingrese la cantida de bolivares que desea cambiar: ")
        try:
            bolivares = float(bolivares)
            valorDolar = 24.40
            dolares = bolivares/valorDolar
            dolares = round(dolares,2)
            print("******************************************************************************")
            print(f"                    La cantidad de $ son: {dolares}                          ")
            print("******************************************************************************\n")
        except ValueError:
            print("error")

conversor()
