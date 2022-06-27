from Productos import Producto
from Pedidos import Pedido

producto1 = Producto(1, 'Computador', 2500000)
producto2 = Producto(2, 'Lavadora', 1500000)
producto3 = Producto(3, 'Nevera', 3650000)

""" productos = [producto1, producto2, producto3]
cantidades = [18, 22, 3] """

pedido = Pedido()

try:
    pedido.agregar_producto(producto1, 5)
    pedido.agregar_producto(producto2, 5)
    pedido.agregar_producto(producto3, 5)
    
    print('Total pedido: ' + str(pedido.total_pedido()))
    pedido.mostrar_pedido()
    
    pedido.eliminar_producto(producto1)
    
    print('Total pedido: ' + str(pedido.total_pedido()))
    pedido.mostrar_pedido()
    
except Exception as e:
    print(e)

