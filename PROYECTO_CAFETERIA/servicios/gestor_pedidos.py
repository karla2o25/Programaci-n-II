from modelos.pedido import Pedido

class GestorPedidos:
    
    def __init__(self):
        self.pedidos = []

    def realizar_pedido(self, cliente, *producto):
        nuevo_pedido = Pedido(cliente)
        for p in producto:
            nuevo_pedido.agregar_producto(p)
        self.pedidos.append(nuevo_pedido)
        print(f"Pedido registrado")


    def listar_pedidos(self):
        if not self.pedidos:
            print("No hay pedidos registrados aún")
        for pedido in self.pedidos:
            print(pedido)
