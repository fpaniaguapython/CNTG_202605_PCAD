# Leer un post de una red social
with open('ejercicio_18_post.txt', mode='rt', encoding='utf-8') as fichero:
    post = fichero.read() # Lee TODO el fichero
    post=post.replace('.','').replace(',','')
    palabras_post = post.split() # Obtenemos una lista con todas las palabras
    conjuntos_palabras_post = set(palabras_post)
print(conjuntos_palabras_post)