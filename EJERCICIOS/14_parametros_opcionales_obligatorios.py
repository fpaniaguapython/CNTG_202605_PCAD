# def saludar(nombre, idioma='Inglés'): # OK
def saludar(nombre='Jesús', idioma='Inglés'): # OK
# def saludar(nombre='Jesús', idioma): # KO
    print(f'Hola {nombre} en {idioma}')

saludar()
saludar('Javier')
saludar('Javier', 'Francés')
saludar(nombre='Javier', idioma='Alemán')
saludar(idioma='Griego')

# Definir una función que reciba:
# 3 argumentos posicionales: x, y, z
# 2 argumentos con valores por defecto: 
    # dimensiones con valor 2 y gravedad con valor 9.8
# Retorna un valor float
def calcular(x: float, y: float, z: float, dimensiones=2, gravedad=9.8) -> float:
    return None

