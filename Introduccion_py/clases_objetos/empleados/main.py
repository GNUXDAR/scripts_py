""" app de gestion de empleados """
from empleado import Empleado
from departamento import Departamento
from empresa import Empresa

# Crear empleados
empleado1 = Empleado('Juan', 3000)
empleado2 = Empleado('Angel', 2500)
empleado3 = Empleado('Luis', 2000)

# Crear departamentos
departamento1 = Departamento('Ventas', [empleado1, empleado2])
departamento2 = Departamento('Finanzas', [empleado3])

# Crear empresa
empresa = Empresa('AC Tecnology', [departamento1, departamento2], 'arturocabrera.com')

# Obtener información de la empresa
print(empresa.obtener_informacion())
