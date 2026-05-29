ingredientes = {'Queso', 'Galleta', 'Huevo', 'Queso', 'Azúcar', 'Mantequilla', 'Sal', 'Azúcar'}
# Es mutable
# Heterogéneos
# No admite duplicados
# No tiene orden
print(ingredientes)

# Añadir elementos
ingredientes.add('Nata')

# Preguntar si contiene un elemento
tiene_sal = 'Sal' in ingredientes
print(tiene_sal)

# Método intersection
alergias = {'Huevo','Harina','Leche'}.intersection({'Huevo'})
print(alergias)
print(len(alergias))


