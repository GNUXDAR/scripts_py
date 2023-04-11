# 00. Concatene la cadena 'I', 'am', 'elearning', 'Python' en una sola cadena, 'Treinta días de Python'.
divide_string = ['I', 'am', 'elearning', 'Python']
print(' '.join(divide_string)) # I am elearning Python

# 01. Declare una variable llamada 'company' y asígnele un valor inicial "Codificación para todos". Imprime la empresa variable usando print(). 
# Imprima la longitud de la cadena de la empresa usando el método len() e print().
company = 'Codificación para todos'
print(len(company))

# 02. Cambie todos los caracteres a letras mayúsculas usando el método upper().
print(company.upper())  # CODIFICACIÓN PARA TODOS

# 03. Cambie todos los caracteres a letras minúsculas usando el método lower().
print(company.lower())  # codificación para todos

# 04. Use los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena "Coding For All".
words = 'Me estoy preparando para el futuro.'
print(words.capitalize())   # Me estoy preparando para el futuro.
print(words.title())        # Me Estoy Preparando Para El Futuro.
print(words.swapcase())     # mE ESTOY PREPARANDO PARA EL FUTURO.

# 05. Verifique si la cadena 'Coding For All' contiene una palabra 'Coding' usando el método index, find u otros métodos.
words = 'Coding For All'
print(words.index('Coding'))    # 0
print(words.find('Coding')) # 0
print('Coding' in words)    # True

# 06. Reemplace la palabra codificación en la cadena 'Codificación para todos' por Python.
new_words = words.replace(words, 'Python')
print(new_words)    # Python

# 07. Divida la cadena 'Codificación para todos' usando el espacio como separador (split()) .
words = 'Coding For All'
new_words = words.split(' ')
print(new_words)    # ['Coding', 'For', 'All']

# 08. 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' divide la cadena en la coma.
words = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
new_words = words.split(', ')
print(new_words)    # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
new_words = words.split(', ,')
print(new_words)    # ['Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon']

# 09. Cree un acrónimo o una abreviatura para el nombre 'Python For Everyone'.
words = 'Python For Everyone'
acronym = ''.join(word[0] for word in words.upper().split())
print(acronym)

# 10. '   Codificación para todos      '  , elimine los espacios finales izquierdo y derecho en la cadena dada.
words = '   Codificación para todos      '
print(words)
print(words.strip())