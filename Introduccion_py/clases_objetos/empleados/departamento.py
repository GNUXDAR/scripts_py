class Departamento:
    def __init__(self, nombre, empleados):
        self.nombre = nombre
        self.empleados = empleados

    def obtener_informacion(self):
        info_empleados = '\n'.join([empleado.obtener_informacion() for empleado in self.empleados])
        return f'Departamento: {self.nombre}\nEmpleados:\n{info_empleados}'
