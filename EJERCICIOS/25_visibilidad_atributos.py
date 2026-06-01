class Contrato:
    def __init__(self, nombre_empleado, categoria, salario):
        self.nombre_empleado = nombre_empleado
        self.categoria = categoria
        self.__salario = salario #Atributo privado
    
    def get_salario(self):
        return self.__salario
    
    def set_salario(self, nuevo_salario):
        if nuevo_salario > self.__salario*1.2:
            raise ValueError('No se puede incrementar el salario en más de un 20%')
        self.__salario = nuevo_salario


mi_contrato = Contrato('Fernando', 'Profesor', 120_000)
mi_contrato.nombre_empleado
mi_contrato.categoria
mi_contrato.__salario