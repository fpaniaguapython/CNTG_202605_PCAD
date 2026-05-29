dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
# Es mutable
# Admite datos heterogéneos

# Acceso de lectura -> 'Miércoles'
dias_semana[2] 
# Modificación
dias_semana[3]='Xoves' 
# Recorrer días
for dia in dias_semana:
    print(dia)
# Agregar días al final
dias_semana.append('Domingo')
# Insertar un día en una posición concreta
dias_semana.insert(5, 'Sábado')
print(dias_semana)
# Borrar elemento
dias_semana.remove('Lunes')
print(dias_semana)
# Eliminar el elemento 2 de la lista
del dias_semana[2]
print(dias_semana)
# Ordenación de listas
lista_ordenada = sorted(dias_semana) # Devuelve una copia ordenada de la lista original
dias_semana.sort() # Ordena la lista
print(dias_semana)
# Obtener información sobre la existencia de un valor
tiene_martes = 'Martes' in dias_semana
