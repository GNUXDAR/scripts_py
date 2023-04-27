# 00. Una a it_companies con una cadena '#'
it_companies = ['AC Tecnology', 'Microsoft', 'Google', 'Twitter', 'Facebook']
print('# '.join(it_companies))  # AC Tecnology# Microsoft# Google# Twitter# Facebook

# 01. Imprimir la primera, segunda y última empresa
print(it_companies[0], it_companies[1], it_companies[-1])

# 02. Imprimir el número de empresas en la lista
print(len(it_companies))

# 03. Compruebe si una determinada empresa existe en la lista it_companies.
if 'Microsoft' in it_companies:
    print('Microsoft Existe en la lista')   # Microsoft Existe en la lista
print(it_companies.index('Microsoft'))  # 1

# 04. Ordenar la lista usando el método sorted()
new_list = sorted(it_companies)
print(new_list) # ['AC Tecnology', 'Facebook', 'Google', 'Microsoft', 'Twitter']

# 05. Invierta la lista en orden descendente usando el método reverse()
print(sorted(it_companies, reverse=True))   # ['Twitter', 'Microsoft', 'Google', 'Facebook', 'AC Tecnology']

# 06. Eliminar la ultima empresa de TI de la lista
# it_companies.remove(it_companies[-1])
it_companies.pop()
print(it_companies)

# 06. Eliminar la empresa o empresas intermedias de TI de la lista
it_companies = ['AC Tecnology', 'Microsoft', 'Google', 'Twitter', 'Facebook']
num_companies = len(it_companies)//2
it_companies.remove(it_companies[num_companies])
print(it_companies)

# 07. Une las siguientes listas
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB', 'PHP']
technologies = front_end + back_end
print(technologies)

# 08. Después de unir las listas en el punto anterior. Copie la lista unida y asígnela a una variable full_stack. Luego inserte Python y SQL después de Redux.
full_stack = technologies
full_stack.insert(4, 'Python')
full_stack.insert(5, 'SQL')
print(full_stack)

# 09. Destruye la lista de empresas de TI
# del it_companies  # al ser eliminada, ya no existe en memoria y no s epuede acceder
it_companies.clear() # [] para vaciar la list
print(it_companies)

# 10. La siguiente es una lista de las edades de 10 estudiantes:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Ordena la lista y encuentra la edad mínima y máxima.
print(min(ages))  # 19
print(max(ages))  # 26

# Agrega la edad mínima y la edad máxima nuevamente a la lista.
ages.append(19)
ages.append(26)
print(ages)        # [19, 22, 19, 24, 20, 25, 26, 24, 25, 24, 19, 26]

# Encuentra la edad promedio(suma de todos los elementos dividida por su cantidad).
i = 0
for age in ages:
    i += age
print(i)            # 273 (con los elementos que se agregaron)

# Encuentra el rango de edades(máximo menos mínimo).
n_min = min(ages)    # 19
n_max = max(ages)    # 26
n_total = n_max - n_min
print(n_total)  # 7