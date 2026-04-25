class Producto:

    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def getNombre(self):
        return self._nombre
    
    def getPrecio(self):
        return self._precio

    def __str__(self):
        return f"{self._nombre}  ${self._precio}\n"
