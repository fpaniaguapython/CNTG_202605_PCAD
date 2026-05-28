def sumar(numero_1: int, numero_2: int) -> int:
    '''
    Sumar dos números enteros.

    Parámetros:
    - numero_1 : primer sumando, debe ser positivo
    - numero_2 : segundo sumando, debe ser positivo

    Return:
    - Suma de los dos parámetros
    '''
    assert isinstance(numero_1, int), 'numero_1 no es entero'
    assert numero_1>0, 'numero_1 debe ser positivo'
    resultado = numero_1 + numero_2
    return resultado

sumar(5, 2)


