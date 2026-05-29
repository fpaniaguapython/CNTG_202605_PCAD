# Película, Serie, Documentales
# Clientes, Actores, Directores
# ¿Idiomas?, Valoraciones, Facturas
# Listas, Cuenta, Favoritos...
class Pelicula:
    def __init__(self, titulo:str, genero:str, duracion:int, anyo:int, premiado=False):
        # Atributos
        self.titulo = titulo
        self.genero = genero
        self.duracion = duracion
        self.anyo = anyo
        self.premiado = premiado

    def get_minutos_anuncios(self, ratio:float):
        numero_minutos_anuncios = self.duracion//ratio
        return numero_minutos_anuncios

# Crear una instancia u objeto - INSTANCIAR
rambo = Pelicula('Rambo', 'Acción', 90, 1982, True) 
minutos_anuncios = rambo.get_minutos_anuncios(10)
print(minutos_anuncios)


