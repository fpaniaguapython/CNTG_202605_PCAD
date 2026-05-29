import re
# Leer un post de una red social
with open('ejercicio_18_post.txt', mode='rt', encoding='utf-8') as fichero:
    post = fichero.read() # Lee TODO el fichero
    
    # Opción 1 - Usando métodos de str
    #post=post.replace('.','').replace(',','')
    #palabras_post = post.split() # Obtenemos una lista con todas las palabras
    
    # Opción 2 - Usando expresiones regulares
    palabras_post = re.findall(r'\w+', post)
    conjunto_palabras_post = set(palabras_post)

with open('ejercicio_18_palabras_censurables.txt', mode='rt', encoding='utf-8') as fichero:
    #palabras = fichero.read() # Lee TODO el fichero
    palabras = fichero.readlines()
    palabras = [palabra.strip() for palabra in palabras] # List comprenhesion
    palabras = set(palabras)

conjunto_interseccion = conjunto_palabras_post.intersection(palabras)
if len(conjunto_interseccion)==0:
    print('PUBLICADO')
else:
    print('CENSURADO')