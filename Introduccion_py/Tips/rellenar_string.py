password = 'python'

print(f'La clave es: {password}')

print(f'{password:*>10}')   # completara hasta 10 con el caracter que querramos
print(f'{password:*<10}')



# rellenar con ceros
numero = 10.14

print(f'{numero}')
print(f'{numero:0<8}')

# rellenar fechas YYYMMDD
year = 2023
month = 6
day = 8
print(f'{year}-{month:0>2}-{day:0>2}')  
# completara con 0 el mes y año
