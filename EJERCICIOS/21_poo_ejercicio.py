'''
Definir la clase Factura:
Atributos:
- Número
- Precio Unitario del producto
- Unidades del producto
- IVA (%)
Métodos:
- get_importe_total
- get_importe_impuesto
'''

class Factura:
    def __init__(self, numero: int, precio_unitario: float, unidades:int, iva:int):
        self.numero = numero
        self.precio_unitario = precio_unitario
        self.unidades = unidades
        self.iva = iva

    def get_importe_impuesto(self) -> float:
        importe_impuesto = self.precio_unitario * self.unidades * (self.iva / 100)
        return importe_impuesto

    def get_importe_total(self) -> float:
        importe_total = self.precio_unitario * \
            self.unidades + \
            self.get_importe_impuesto()
        return importe_total

    
factura_1 = Factura(100, 10, 100, 21)
print(factura_1.get_importe_impuesto())
print(factura_1.get_importe_total())

    
