lista = [5, 4, 8, 10, 11]

# Opción 'tradicional'
def es_suficiente(numero):
    return numero>7

lista_filtrada = filter(es_suficiente, lista)

# Opción 'lambda'
lista_filtrada = filter(lambda numero : numero>7, lista)