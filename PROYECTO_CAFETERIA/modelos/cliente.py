from abc import ABC, abstractmethod

class Cliente(ABC):

    def __init__(self, nombre, identificador):
        self._nombre = nombre
        self._identificador = identificador
        self._descuento = 10
    
    @abstractmethod
    def __str__(self):
        pass
