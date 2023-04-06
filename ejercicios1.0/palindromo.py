# Un palíndromo, también llamado palíndroma o palindroma, es una palabra o frase que se lee igual en un sentido que en otro.
# Ejemplos: Reconocer,Somos o no somos, Isaac no ronca asi, Sé verlas al revés, Amo la paloma, Anita lava la tina, Luz azul, Yo hago yoga hoy, Ana lava lana
def delete_space(text):
    new_text = text.lower().replace(" ", "")
    return new_text

def reverse(text):
    reverse_text = ""
    for l in text:
        reverse_text = l + reverse_text # la clave es poner al iterador "l" antes: {l + reverse_text} en vez de {reverse_text + l}
    return reverse_text


def es_palindromo(text):
    text = delete_space(text)
    reverse_text = reverse(text)
    
    return reverse_text == text


print(es_palindromo("Sé verlas al revés"))
