# CLASES Y OBJETOS 2

"""class Cuadrado:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        area = self.ancho * self.alto
        return area

figura = Cuadrado(10, 12)

print(figura.alto)
print(figura.calcular_area())"""

# Herencia en POO
class Persona:
    def __init__(self, nombre, apellido, cedula, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono

class Empleado(Persona):
    def __init__(self, nombre, apellido, cedula, telefono, salario):
        super().__init__(nombre, apellido, cedula, telefono)
        self.salario = salario

class Cliente(Persona):
    def __init__(self, nombre, apellido, cedula, telefono, categoria):
        super().__init__(nombre, apellido, cedula, telefono)
        self.categoria = categoria

emp = Empleado('Arturo', 'Cabrera', 123456, 2424242424, 3000)
cli = Cliente('Arturo', 'Cabrera', 123456, 2424242424, 'vip')


print(emp.nombre)
print(cli.categoria)

# Lo ideal es que cada Class vaya en un fichero independiente, por lo general el fichero se llamra como se llama la clase, pero en mi nuscula
# ejemplo: miClass el fichero se llmaria mi_class.py
# como lo haremos en el directorio /clases_objetos
