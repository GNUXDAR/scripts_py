""" 
pip3 install pywhatkit
sudo apt-get install python3-tk python3-dev
"""
import pywhatkit

# Convertir imagen en arte ASCII
pywhatkit.image_to_ascii_art('../img/ACTECNOLOGY.png', 'img_file')

# Leer archivo con arte ASCII
with open('img_file.txt', 'r') as f:
    ascii_art = f.read()

# Imprimir arte ASCII en la consola
print(ascii_art)
