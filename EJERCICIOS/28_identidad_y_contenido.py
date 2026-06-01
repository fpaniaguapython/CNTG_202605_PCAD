x = 'Python'
y = 'Py'
y = y + 'thon'
print(x==y) # Comparación de contenido
print(x is y) # Comparación de identidad

class Computadora:
    def __init__(self, nombre, velocidad):
        self.nombre = nombre
        self.velocidad = velocidad

    def __eq__(self, other):
        print('Ejecutando __eq__')
        return self.velocidad==other.velocidad

computadora_1 = Computadora('Lenovo', 2.4)
computadora_2 = Computadora('HP', 2.4)
print(computadora_1 is computadora_2) # False
print(computadora_1==computadora_2) # False        