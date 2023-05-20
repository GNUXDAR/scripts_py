class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def obtener_informacion(self):
        return f'Nombre: {self.nombre}, Salario: {self.salario}'
