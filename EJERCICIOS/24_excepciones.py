def sumar(sumando_1 : int, sumando_2 : int) -> int:
    if (not isinstance(sumando_1, int)):
        raise TypeError('El sumando_1 no es entero')
    if (not isinstance(sumando_2, int)):
        raise TypeError('El sumando 2 no es entero')
    if sumando_1<0 or sumando_2<0:
        raise ValueError('Alguno de los dos argmentos es negativo')
    resultado = sumando_1 + sumando_2
    return resultado

try:
    resultado = sumar('1', -2)
    print(resultado)
except ValueError as ve:
    # Este bloque se ejecuta si ha ocurrido un error de tipo TypeError
    print(ve)
except TypeError as te:
    # Este bloque se ejecuta si ha ocurrido un error de tipo TypeError
    print(te)
except BaseException as be:
    print('Ha ocurrido un error desconocido. Contacte con el administrador')
finally:
    print('Esto se ejecuta SIEMPRE')
