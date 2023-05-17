texto = ''
while texto != 'salir':
    texto = texto = input('> ')
    texto = texto.replace(' :) ', ' 🙂 ')
    texto = texto.replace(' =D ', ' 😂 ')
    texto = texto.replace(' :P ', ' 😋 ')
    texto = texto.replace(' :p ', ' 😋 ')
    texto = texto.replace(' :( ', ' 😩 ')
    texto = texto.replace(' :| ', ' 😐 ')
    texto = texto.replace(' :* ', ' 😘 ')
    texto = texto.replace(' <3 ', ' 😍 ')
    texto = texto.replace(' B ', ' 😎 ')
    print(texto)
    print('')