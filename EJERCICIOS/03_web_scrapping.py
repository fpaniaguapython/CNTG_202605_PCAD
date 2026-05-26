import requests

from bs4 import BeautifulSoup

import re

def obtener_pib_fmi_singapur(html: str) -> str | None:
    """
    Recibe el HTML de la página de Wikipedia y devuelve
    el PIB per cápita estimado por el FMI de Singapur.

    Retorna:
        - El valor como string (ej: "92 932")
        - None si no lo encuentra
    """

    soup = BeautifulSoup(html, "html.parser")

    # Buscar todas las tablas wikitable
    tablas = soup.find_all("table", class_="wikitable")

    for tabla in tablas:
        filas = tabla.find_all("tr")

        for fila in filas:
            columnas = fila.find_all(["td", "th"])

            # Convertir a texto limpio
            textos = [c.get_text(" ", strip=True) for c in columnas]

            # Buscar fila de Singapur
            if any("Singapur" in t for t in textos):

                # Buscar posibles valores numéricos del FMI
                numeros = [
                    t for t in textos
                    if re.search(r"\d", t)
                ]

                # Normalmente el primer número corresponde al FMI
                if numeros:
                    return numeros[0]

    return None


URL = 'https://es.wikipedia.org/wiki/Anexo:Pa%C3%ADses_por_PIB_(nominal)_per_c%C3%A1pita'

headers = {
    "User-Agent": "MiAplicacion/1.0 (admin@midominio.com)"
}

response = requests.get(url=URL, headers=headers)

if response.status_code == 200:
    datos = response.text
    pib_estimado_singapur = obtener_pib_fmi_singapur(datos)
    print(pib_estimado_singapur)
else:
    print('Ha ocurrido un error', response.status_code)