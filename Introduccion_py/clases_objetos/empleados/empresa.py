class Empresa:
    def __init__(self, nombre, departamentos, web):
        self.nombre = nombre
        self.departamentos = departamentos
        self.web = web

    def obtener_informacion(self):
        info_departamentos = '\n'.join([departamento.obtener_informacion() for departamento in self.departamentos])
        return f'Empresa: {self.nombre}\nDepartamentos:\n{info_departamentos}\nWebsite:\n{self.web}'
