class Persona:
    def __init__(self, nombre, apellido, cedula, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self) -> str:
        """ lo que se imprime por defecto si intentamos imprimir el objeto """
        return 'Cargado: ' + self.nombre + ' ' + self.apellido + '-' + self.cedula
