# Pedir el API_KEY en https://www.omdbapi.com/
# La mía se gasta.

import requests

URL = 'https://www.omdbapi.com'
API_KEY = '95c08eba'
params = {
    'apikey': API_KEY,
    't':'Batman'
}

response = requests.get(url=URL, params=params)

if response.status_code == 200:
    datos = response.json()
    print(datos)
else:
    print('Ha ocurrido un error')