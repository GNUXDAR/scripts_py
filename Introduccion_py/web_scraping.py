# Que es el Web Scraping
# Internet está lleno de una gran cantidad de datos que se pueden utilizar para diferentes propósitos. 
# Para recopilar estos datos, necesitamos saber cómo extraer datos de un sitio web.
# El web scraping es el proceso de extraer y recopilar datos de sitios web y almacenarlos en una máquina local o en una base de datos.
# En esta sección, usaremos beautifulsoup y Requests Package para extraer datos. La versión del paquete que estamos usando es beautifulsoup 4.
# Para comenzar a rastrear sitios web, necesita request, beautifoulSoup4 y un sitio web.
# pip install requests
# pip install beautifulsoup4

# Para extraer datos de sitios web, se necesita una comprensión básica de las etiquetas HTML y los selectores CSS. 
# Nos dirigimos al contenido de un sitio web mediante etiquetas HTML, clases o identificadores. Importemos el módulo request y BeautifulSoup

# import requests
# from bs4 import BeautifulSoup

# Declaremos la variable url para el sitio web que vamos a raspar.
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'
# Usemos el método de obtención de solicitudes para obtener los datos de la URL
response = requests.get(url)
# vamos a comprobar el estado
status = response.status_code
print(status)  # 200 significa que la búsqueda fue exitosa

# Usando beautifulSoup para analizar el contenido de la página
import requests
from bs4 import BeautifulSoup
# url = 'https://archive.ics.uci.edu/ml/datasets.php'
url = 'https://arturocabrera.com'

response = requests.get(url)
content = response.content  # obtenemos todo el contenido del sitio web
soup = BeautifulSoup(content, 'html.parser') # hermosa sopa le dará la oportunidad de analizar
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body)  # da toda la página en el sitio web
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# Estamos apuntando a la tabla con el atributo cellpadding con el valor de 3 
# Podemos seleccionar usando id, clase o etiqueta HTML, para obtener más información, consulte el documento beautifulsoup
table = tables[0]  # el resultado es una lista, estamos sacando datos de ella
for td in table.find('tr').find_all('td'):
    print(td.text)