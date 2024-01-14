
"""fichero de prueba"""
# convertir caractee a codigo ascii y a binario
# https://elcodigoascii.com.ar/

# Codigo de caracteres ASCII
# letra = "a"
# print(ord(letra))
# print(chr(43))
# bromecina para la gripe

# comprension de listas
# user_list2 = ['user00', 'user01', 'user02', 'user03', 'user04', 'user05']
# to_delete = ['user00', 'user02']

# new_list = [item for item in user_list2 if item not in to_delete]
# print(new_list)
# class Person:
#     def __init__(self, firstname='Arturo', lastname='Cabrera', age=33, country='Venezuela', city='Chacaracual'):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age
#         self.country = country
#         self.city = city
#         self.skills = []

#     def person_info(self):
#         return f'{self.firstname} {self.lastname} tiene {self.age} de edad. Vive en {self.country}, {self.city}'

#     def add_skill(self, skill):
#         self.skills.append(skill)
# class Student(Person):
#     pass


# s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
# s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)


# class Student(Person):
#     def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki', gender='male'):
#         self.gender = gender
#         super().__init__(firstname, lastname, age, country, city)

#     def person_info(self):
#         gender = 'He' if self.gender == 'male' else 'She'
#         return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'


# s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
# s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
# print(s1.person_info())
# s1.add_skill('JavaScript')
# s1.add_skill('React')
# s1.add_skill('Python')
# print(s1.skills)

# print(s2.person_info())
# s2.add_skill('Organizing')
# s2.add_skill('Marketing')
# s2.add_skill('Digital Marketing')
# print(s2.skills)

# class Figura:
#     def area(self):
#         pass


# class Cuadrado(Figura):
#     def __init__(self, lado):
#         self.lado = lado

#     def area(self):
#         return self.lado * self.lado


# class Circulo(Figura):
#     def __init__(self, radio):
#         self.radio = radio

#     def area(self):
#         return 3.1416 * self.radio * self.radio


# # cuadrado = Cuadrado(5)  # Crea una instancia de la clase Cuadrado con un lado de 5
# # area_cuadrado = cuadrado.area()  # Llama al método area() en la instancia de Cuadrado creada
# # print(area_cuadrado)  # Imprime el resultado del cálculo del área del cuadrado

# # circulo = Circulo(3)  # Crea una instancia de la clase Circulo con un radio de 3
# # area_circulo = circulo.area()  # Llama al método area() en la instancia de Circulo creada
# # print(area_circulo)  # Imprime el resultado del cálculo del área del círculo

# cuadrado = Cuadrado(5)
# circulo = Circulo(3)

# print(cuadrado.area())  # 25
# print(circulo.area())  # 28.2744

# imprimir 100 veces
# for i in range(101, 200):
#     print('Meryuris ', i)

# # gastos de Meryuris en una lista
# monto_total = 244.75
# comprar = [15, 8, 10, 50, 32.63]
# gasto = 0

# for m in comprar:
#     gasto += m
# print(gasto)
# print(monto_total - gasto)

# # gastos de Meryuris en un diccionario
# monto_total = 244.75
# comprar = {
#     'meyo': 15,
#     'cole': 8,
#     'yo': 10,
#     'cajero': 50,
#     'supermaxi': 32.63
# }
# gasto = 0

# imprimir la clave 
# for clave in comprar:
#     print(clave)

# # imprimir el valor del dict
# for clave in comprar:
#     valor = comprar[clave]
#     gasto += valor
#     print(valor)
# print(monto_total - gasto)


# # Como crear un array multidimensional desde cero
# array_datos = [[]]
# array_datos[0].append('Arturo')
# array_datos[0].append('Cabrera')

# array_datos.append([])
# array_datos[1].append('gnuxdar')
# array_datos[1].append('AC Tecnology')

# array_datos.append([])
# array_datos[2].append('Ecuador')
# array_datos[2].append('Venezuela')
# print(array_datos)
# print('La cantidad es de: ', len(array_datos[0]))


# # gastos de Meryuris en una lista
# monto_total = 244.75
# comprar = [15, 8, 10, 50, 32.63]
# gasto = 0

# for m in comprar:
#     gasto += m
# print(gasto)
# print(monto_total - gasto)

# # HAACER CALCULOS CON UN DICCIONARIO
# monto_total = 244.75
# comprar = {
#     'meyo': 15,
#     'cole': 8,
#     'yo': 10,
#     'cajero': 50,
#     'supermaxi': 32.63
# }
# gasto = 0

# imprimir la clave
# for clave in comprar:
#     print(clave)

# # imprimir el valor del dict
# for clave in comprar:
#     valor = comprar[clave]
#     gasto += valor
#     print(valor)
# print(monto_total - gasto)

nombres = ['Alexander', 'Aleaxa', 'Meryuris', 'Arturo']
apellido = ['Cabrera']

result = ' '.join(nombres)

print(result)