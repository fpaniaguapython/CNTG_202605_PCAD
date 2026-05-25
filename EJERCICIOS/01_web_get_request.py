import requests

URL = 'https://datos.gob.es/es/catalogo/a12002994-oficinas-rurales.csv'

response = requests.get(url=URL)

if response.status_code == 200:
    # 200 -> OK
    print('Ha ido bien')
    datos = response.text
    print(datos)
else:
    # ERROR
    print('Ha ocurrido un error')