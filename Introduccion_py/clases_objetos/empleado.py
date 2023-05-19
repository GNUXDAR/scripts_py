from persona import Persona

class Empleado(Persona):
    def __init__(self, nombre, apellido, cedula, telefono, salario):
        super().__init__(nombre, apellido, cedula, telefono)
        self.salario = salario
