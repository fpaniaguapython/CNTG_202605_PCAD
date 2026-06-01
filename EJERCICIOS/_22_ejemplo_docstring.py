def read_file(file_name : str) -> str:
    """Proporciona el contenido textual de un fichero

    Params:
    - file_name : nombre del fichero.

    Return:
    - Una cadena de caracteres con el contenido del fichero.
    """
    with open(file_name, mode='rt', encoding='utf-8') as fichero:
        data = fichero.read()
    return data