diccionario = {
    'Raul':('Wolkswagen',2009,230,True),
    'Fernando':('Seat',2004,140,False),
    'Laura':('Renault',2010,150,True),
    'Javier':None
}
# Heterogéneo
# La clave tiene que ser única
# Los valores pueden ser duplicados
# El orden no influye
# Es mutable

# Acceso
print(diccionario['Laura'])
# Añadir elemento
diccionario['Carmen']=('Toyota',2012,190)
# Recorrer claves
for clave in diccionario.keys():
    pass

# Recorrer valores
for valor in diccionario.values():
    pass

# Recorrer claves y valores
for clave, valor in diccionario.items():
    pass


