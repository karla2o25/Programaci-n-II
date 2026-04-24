from figura import Figura

class Cuadrado(Figura):

    def __init__(self, lado):
        self.lado = lado
    
    def CalcularArea(self):
        return self.lado**2
    
    def CalcularPerimetro(self):
        return self.lado*4
    
