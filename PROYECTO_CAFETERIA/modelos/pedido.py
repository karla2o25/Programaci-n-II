from modelos.producto import Producto
from modelos.cliente_frecuente import ClienteFrecuente

class Pedido:

    def __init__(self, cliente):
        self._cliente = cliente
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)
        return f"Productos añadidos a tu orden"

    def calcular_total(self):
        total = 0
        subtotal = 0
        for producto in self._productos:
            subtotal += producto._precio

        total = subtotal - (subtotal *(self._cliente._descuento / 100))
        return total

    def __str__(self):
        resumen = f"Pedido de {self._cliente}\n"
        resumen += "Orden:\n"

        for i in self._productos:
            resumen += f" - {i}"

        resumen += f"Total a pagar: ${self.calcular_total()}\n"
        return resumen
