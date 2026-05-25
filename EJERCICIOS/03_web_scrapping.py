import requests
from bs4 import BeautifulSoup

URL = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_PIB_(nominal)_per_c%C3%A1pita'

headers = {
    "User-Agent": "MiAplicacion/1.0 (admin@midominio.com)"
}

response = requests.get(url=URL, headers=headers)

if response.status_code == 200:
    datos = response.text
    soup = BeautifulSoup(datos, 'html.parser')
else:
    print('Ha ocurrido un error', response.status_code)