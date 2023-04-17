try:
  valor = input('Escribe el número: ') #pero el usuario lo pone con letras
  valorNumerico = int(valor)
  resultado = valorNumerico + 3
  print(resultado)
except Exception as e:
    print('Hemos subrido un error debido a que: ',str(e))


# tipos de errores
try:
  valor = input('Introduce un valor: ') 
  valorNumerico = int(valor) #/0 #/dos
  resultado = 0 / valorNumerico 
  print(resultado)
except ArithmeticError:
  print('Error aritmético')
except ValueError:
    valorNumerico = 0
except Exception as e:
   print('Hemos subrido un error debido a que:',str(e))

print(valorNumerico + 3)

# Escribe una función llamada check-season, toma un parámetro de mes y devuelve la estación: Otoño, Invierno, Primavera o Verano.
def check_season(month):
    # abril, mayo y junio -> primavera
    # julio, agosto y septiembre. -> verano
    # octubre, noviembre y diciembre. -> otoño
    # enero, febrero y marzo. -> invierno
    month = month.lower()
    try:
        if month == 'abril' or month == 'mayo' or month == 'junio':
            print('Primavera')
        elif month == 'julio' or month == 'agosto' or month == 'septiembre':
            print('verano')
        elif month == 'octubre' or month == 'noviembre' or month == 'diciembre':
            print('otoño')
        elif month == 'enero' or month == 'febreo' or month == 'marzo':
            print('invierno')
        else:
            raise ValueError('Mes no valido')
    except ValueError as error:
        print(error)
        # print('Le invito a que revise bien lo que ingreso', month)


check_season('abril')

"""
En Python, raise se utiliza para generar una excepción específica en un bloque de código. 
Cuando se utiliza raise en un bloque try-except, se puede especificar el tipo de excepción que se va a generar 
y opcionalmente se puede proporcionar un mensaje detallado para indicar la causa de la excepción.
"""
