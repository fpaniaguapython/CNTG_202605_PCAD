def calcular_importe():
    pass

def calcular_importe(numero):
    pass

def calcular_importe(numero_1, numero_2):
    pass

def calcular_importe(numero_1, numero_2=10):
    pass

def calcular_importe(numero_1=14, numero_2=10):
    pass

#def calcular_importe(numero_1=14, numero_2): # Error
#    pass

def calcular_importe(*args):
    pass

calcular_importe(10,15,10,12,18,50)

# Escribir un función que reciba como argumentos:
# - Lista
# - Un número entero
# La función añade el número a la lista
# La función no tiene retorno

# Llamar a la función y mostrar el valor de la lista después
# de la llamada

def agregador_numero(lista: list, numero: int) -> None:
    lista.append(numero)

valores = [10, 8, 9, 5]
numero = 15
agregador_numero(valores, numero) # Argumentos posicionales (indexed)
agregador_numero(lista=valores, numero=numero) # Keywords arguments
agregador_numero(numero=numero, lista=valores) # Keywords arguments




