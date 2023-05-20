# CLASES Y OBJETOS
# Python es un lenguaje de programación orientado a objetos. Todo en Python es un objeto, con sus propiedades y métodos. 
# Un número, cadena, lista, diccionario, tupla, set, etc. utilizado en un programa es un objeto de una clase incorporada correspondiente. 
# Creamos una clase para crear un objeto. Una clase es como un constructor de objetos o un "plan" para crear objetos. 
# Instanciamos una clase para crear un objeto. La clase define los atributos y el comportamiento del objeto, 
# mientras que el objeto, por otro lado, representa la clase.

# Hemos estado trabajando con clases y objetos desde el comienzo de este desafío sin saberlo. 
# Cada elemento en un programa de Python es un objeto de una clase.

# CREANDO UNA CLASE
# Para crear una clase necesitamos la palabra clave class seguida del nombre y dos puntos. El nombre de la clase debe ser CamelCase.

# syntax
# class ClassName:
#   code goes here

# Ejemplo
class Person:
  pass
print(Person)   #   <class '__main__.Person'>

""" "pass" es una instrucción en Python que no hace nada. Se utiliza como marcador de posición en el código cuando se requiere una instrucción pero no se desea realizar ninguna acción.

Por ejemplo, en una definición de función, se puede utilizar "pass" para indicar que la función aún no está implementada:
"""

# CREANDO UN OBJETO
# Podemos crear un objeto llamando a la clase.
p = Person()
print(p)    # <__main__.Person object at 0x7f0aeb73b1c0>

# CONSTRUCTOR DE CLASES
# En los ejemplos anteriores, hemos creado un objeto de la clase Person. 
# Sin embargo, una clase sin constructor no es realmente útil en aplicaciones reales. 
# Usemos la función constructora para que nuestra clase sea más útil. 
# Al igual que la función constructora en Java o JavaScript, Python también tiene una función constructora init() incorporada. 
# La función constructora __init__ tiene un parámetro propio que es una referencia a la instancia actual de la clase. Ejemplos:


class Person:
    def __init__(self, name):
        # self permite adjuntar parámetros a la clase
        self.name = name


p = Person('Arturo')
print(p.name)
print(p)

# output
# Arturo
# <__main__.Person object at 0x7f9b3ecf7160>

# Agreguemos más parámetros a la función constructora.
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city


p = Person('Arturo', 'Cabrera', 33, 'Venezuela', 'Tunapuy')
print(p.firstname, p.lastname)
print(p.age)
print(p.country)
print(p.city)
# output
# Arturo Cabrera
# 33
# Venezuela
# Tunapuy

# METODOS DE OBJETOS
# Los objetos pueden tener métodos. Los métodos son funciones que pertenecen al objeto.
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Arturo', 'Cabrera', 33, 'Ecuador', 'Quito')
print(p.person_info())   # Arturo Cabrera is 33 years old. He lives in Quito, Ecuador

# METODOS PREDETERMINADOS DE OBJETOS
# A veces, es posible que desee tener valores predeterminados para sus métodos de objeto. 
# Si damos valores predeterminados para los parámetros en el constructor, podemos evitar errores cuando llamamos o instanciamos nuestra clase sin parámetros. 
# Veamos cómo se ve:
class Person:
    def __init__(self, firstname='Arturo', lastname='Cabrera', age=33, country='Ecuador', city='Quito'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'


p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())

# METODO PARA MODIFICAR LOS VALORES PREDETERMINADAS DE LA CLASE
# En el siguiente ejemplo, la clase persona, todos los parámetros del constructor tienen valores predeterminados. 
# Además de eso, tenemos el parámetro de habilidades, al que podemos acceder usando un método. 
# Vamos a crear el método add_skill para agregar habilidades a la lista de habilidades.

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

p1 = Person()
print(p1.person_info())
p1.add_skill('PHP')
p1.add_skill('Python')
p1.add_skill('React')
p1.add_skill('CSS')
p2 = Person('John', 'Doe', 30, 'Finland', 'Helsinki')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
# output
# Arturo Cabrera tiene 33 de edad. Vive en Venezuela, Chacaracual
# John Doe tiene 30 de edad. Vive en Finland, Helsinki
# ['PHP', 'Python', 'React', 'CSS']
# []

# HERENCIA
# Usando la herencia podemos reutilizar el código de la clase principal. 
# La herencia nos permite definir una clase que hereda todos los métodos y propiedades de la clase principal. 
# La clase padre o superclase o clase base es la clase que proporciona todos los métodos y propiedades. 
# La clase secundaria es la clase que hereda de otra clase principal. Vamos a crear una clase de estudiante heredando de la clase de persona.


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

# No llamamos al constructor init() en la clase secundaria. Si no lo llamamos, aún podemos acceder a todas las propiedades desde el padre. 
# Pero si llamamos al constructor, podemos acceder a las propiedades principales llamando a super.
# Podemos agregar un nuevo método al elemento secundario o podemos anular los métodos de la clase principal 
# creando el mismo nombre de método en la clase secundaria. Cuando agregamos la función init(), 
# la clase secundaria ya no heredará la función init() del padre.

# ANULACION DEL METODO PRINCIPAL

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

# Podemos usar la función integrada super() o el nombre del padre Person para heredar automáticamente los métodos y propiedades de su padre. 
# En el ejemplo anterior, anulamos el método principal. El método del hijo tiene una característica diferente, 
# puede identificar si el género es masculino o femenino y asignar el pronombre adecuado (Él/Ella).
