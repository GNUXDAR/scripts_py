try:
  valor = input('Escribe el número:') #pero el usuario lo pone con letras
  valorNumerico = int(valor)
  resultado = valorNumerico + 3
  print(resultado)
except Exception as e:
    print('Hemos subrido un error debido a que:',str(e))


# tipos de errores
try:
  valor = input('Introduce un valor :') 
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