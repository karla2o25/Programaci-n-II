class Cafeteria:
    def __init__(self, nombre):
        self.nombre = nombre
        self._productos_disponibles = []
        self._clientes_registrados = []
        self._pedidos_realizados = []

    def registrar_productos(self, producto):
        self._productos_disponibles.append(producto)
        
