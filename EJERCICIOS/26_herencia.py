"""
En la herencia, BarcoBelico extiende a 
Barco y le dota de nueva funcionalidad
"""
class Barco:
    def __init__(self, nombre, eslora, calado, capacidad):
        self.nombre = nombre
        self.eslora = eslora
        self.calado = calado
        self.capacidad = capacidad

class BarcoBelico(Barco):
    def disparar(self):
        pass

barco = BarcoBelico('San Agustín', 100, 5, 100)
barco.disparar()
