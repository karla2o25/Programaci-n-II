from modelos.cliente import Cliente

class ClienteNormal(Cliente):
    def __init__(self, nombre, identificador):
        super().__init__(nombre, identificador)
        self._descuento = 0

    def __str__(self):
        return f"Cliente normal: {self._nombre} - ID: {self._identificador}"
