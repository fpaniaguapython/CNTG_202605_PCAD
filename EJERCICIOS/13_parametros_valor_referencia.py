def calcular(numero):
    numero=numero+1

def agregar(lista, numero):
    lista.append(numero)

numero=3
lista=[0,1,2]

calcular(numero) # Paso de parámetros por valor (no se modifica la variable)
print(numero)#3

agregar(lista, numero) # Paso de parámetros por referencia (sí se modifica)
print(lista)#[0, 1, 2, 3]