def validar_nit(nit):
    '''Funcion para validar NIT de Guatemala'''
    # Elimina espacios en blanco
    nit_n = nit.replace(' ', '')
    # Elimina el guion del nit
    nit_ok = nit_n.replace('-', '')
    # Base para multiplicar
    base = 1

    # Guarda el digito validador, el ultimo
    dig_validador = nit_ok[-1]
    print("dig_validador ", dig_validador)

    # Guarda el resto de numeros para sumar
    dig_nit = list(nit_ok[0:-1])
    print("dig_nit ", dig_nit)

    # Reverse invierte el orden de los digitos del original
    # El array inverso se refleja al original
    dig_nit_rev = dig_nit.reverse()  # None
    print("El array inverso ", dig_nit_rev)

    try:
        suma = 0
        # Por cada numero del nit en inversa
        for n in dig_nit:
            base += 1
            suma += int(n) * base

        # Guarda el residuo
        resultado = suma % 11
        comprobacion = 11 - resultado

        if suma >= 11:
            resultado = suma % 11
            comprobacion = 11 - resultado

        if comprobacion == 10:
            if dig_validador.upper() == 'K':
                return True

        elif comprobacion == int(dig_validador):
            return True

        else:
            return False

    except:
        return False


if __name__ == '__main__':
    print('Validador NIT')
    nit = str(input('Ingresa el NIT: \n'))
    print(validar_nit(nit))