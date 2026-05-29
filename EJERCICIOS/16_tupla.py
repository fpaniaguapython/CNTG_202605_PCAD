estaciones = ('Primavera', 'Verano', 'Otoño', 'Invierno')
# Es INmutable
# Admite datos heterogéneos

# Acceso de lectura -> 'Otoñoa'
print(estaciones[2])
# Recorrer estaciones
for estacion in estaciones:
    print(estacion)
# Obtener una copia de la tupla ordenada
estaciones_ordenadas = sorted(estaciones)
print(estaciones_ordenadas)
# Obtener información sobre la existencia de un valor
tiene_otoño = 'Otoño' in estaciones