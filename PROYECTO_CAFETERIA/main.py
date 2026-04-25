from modelos.cafeteria import Cafeteria
from modelos.cliente_normal import ClienteNormal
from modelos.cliente_frecuente import ClienteFrecuente
from modelos.cliente import Cliente
from modelos.producto import Producto
from modelos.pedido import Pedido
from servicios.gestor_pedidos import GestorPedidos

#Crear cafetería
cafeteria = Cafeteria("Café de Karlita")

#Crear productos
producto1 = Producto("Malteada de fresa", 50)
producto2 = Producto("Café con leche", 45)
producto3 = Producto("Pay de manzana", 35)
producto4 = Producto("Cuernito", 15)

#Crear clientes
cliente1 = ClienteNormal("Pablo", "500")
cliente2 = ClienteFrecuente("Luz", "501")

#Crear gestor de pedidos
gestor = GestorPedidos()

#Realizar pedido
gestor.realizar_pedido(cliente1, producto1, producto3)
gestor.realizar_pedido(cliente2, producto1, producto2, producto3)

#Imprimir pedido
gestor.listar_pedidos()

#Registrar productos en cafetería
cafeteria.registrar_productos(producto1)
cafeteria.registrar_productos(producto2)
cafeteria.registrar_productos(producto3)
cafeteria.registrar_productos(producto4)