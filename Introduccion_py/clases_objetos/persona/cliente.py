from persona import Persona

class Cliente(Persona):
    def __init__(self, nombre, apellido, cedula, telefono, categoria):
        super().__init__(nombre, apellido, cedula, telefono)
        self.categoria = categoria
