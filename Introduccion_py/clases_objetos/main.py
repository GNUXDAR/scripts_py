from empleado import Empleado
from cliente import Cliente


emp = Empleado('Arturo', 'Cabrera', 123456, 2424242424, 3000)
cli = Cliente('Arturo', 'Cabrera', 123456, 2424242424, 'vip')


print(emp.nombre)
print(cli.categoria)

print(emp) # imprimiendo el objeto


personas = []

def cargar():
    respuesta = input('¿Va a ingresar un empleado? ')
    nombre = input('Ingrese el nombre ')
    apellido = input('Ingrese el apellido ')
    cedula = input('Ingrese la cedula ')
    telefono = input('Ingrese el telefono ')

    if respuesta == 'si':
        salario = input('Ingrese el salario: ')
        emp = Empleado(nombre, apellido, cedula, telefono, int(salario))
        personas.append(emp)
    else:
        tipo = input('Ingrese el tipo de cliente: ')
        cli = Cliente(nombre, apellido, cedula, telefono, tipo)
        personas.append(cli)

# personas = []
cargar()
cargar()

for persona in personas:
    print(persona)