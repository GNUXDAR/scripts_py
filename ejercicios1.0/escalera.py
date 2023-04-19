# * - Crea una función que dibuje una escalera según su número de escalones.
# * - Si el número es positivo, será ascendente de izquiera a derecha.
# * - Si el número es negativo, será descendente de izquiera a derecha.
# * - Si el número es cero, se dibujarán dos guiones bajos(__).
# * Ejemplo: 4
# *         _
# *       _|
# *     _|
# *   _|
# * _|
# *
# */
def escalera():
    try:
        ne = int(input('Ingrese la cantidad de escalones: '))
    except ValueError:
        print('Ingrese un número entero')
        return
    if ne > 20 or ne < -20:
        print('El número de escalones ingresado es demasiado grande.')
    elif ne > 0:
        print('  '*(ne), '_')
        for i in range(ne):
            print('  '*(ne-1),'_| ')
            ne-=1
    elif ne < 0:
        print('_')
        for i in range(abs(ne)):
            print('  '*i,'|_')
    elif ne == 0:
        print('__')

escalera()