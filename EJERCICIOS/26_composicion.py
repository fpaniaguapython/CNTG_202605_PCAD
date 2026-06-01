"""
En la composicón, 
"""
class Lanzacohetes:
    def disparar(self):
        pass

class Barco:
    def __init__(self, nombre, eslora, calado, capacidad, arma):
        self.nombre = nombre
        self.eslora = eslora
        self.calado = calado
        self.capacidad = capacidad
        self.arma = arma

barco = Barco('San Agustín', 100, 5, 100, Lanzacohetes())
barco.arma.disparar()