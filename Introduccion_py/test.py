
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
class Person:
    def __init__(self, firstname='Arturo', lastname='Cabrera', age=33, country='Venezuela', city='Chacaracual'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city
        self.skills = []

    def person_info(self):
        return f'{self.firstname} {self.lastname} tiene {self.age} de edad. Vive en {self.country}, {self.city}'

    def add_skill(self, skill):
        self.skills.append(skill)
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)


class Student(Person):
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)
