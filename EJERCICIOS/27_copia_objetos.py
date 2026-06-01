# https://pythontutor.com/
lista_1 = ['Python', ['Interpretado','Moderno','Sencillo','Multiparadigma']]

# Crear una copia asignando la lista a otra variable
lista_2 = lista_1 # SON LA MISMA LISTA

# Crear una copia haciendo slicing
lista_3 = lista_1[:] # # Shallow copy
lista_1[0]='Java' # Sólo cambia en lista_1
lista_1[1][3]='Orientado a Objetos' # Cambia en las dos listas
print(lista_1)
print(lista_3)

# Crear una copia utilizando el método copy
lista_4 = lista_1.copy() # Shallow copy

# Utilizando el módulo copy y la función deepcopy
import copy
lista_5 = copy.deepcopy(lista_1) # Deep copy --> las dos estructuras son independientes