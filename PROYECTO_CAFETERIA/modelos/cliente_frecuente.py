from modelos.cliente import Cliente

class ClienteFrecuente (Cliente):

    def __init__(self, nombre, identificador):
        super().__init__(nombre, identificador)

    def __str__(self):
        return f"Cliente frecuente: {self._nombre} - ID: {self._identificador} - Descuento - %{self._descuento}"
