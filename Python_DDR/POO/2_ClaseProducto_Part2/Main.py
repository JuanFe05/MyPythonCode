from Productos import Producto
from Pedidos import Pedido

producto1 = Producto(1, 'Computador', 2500000)
producto2 = Producto(2, 'Lavadora', 1500000)
producto3 = Producto(3, 'Nevera', 3650000)

""" print(producto1.nombre)
print(producto2.precio)
print(producto3)

print(producto1.calcularTotal(5))
print(producto2.calcularTotal(10))
print(producto3.calcularTotal(28)) """

productos = [producto1, producto2, producto3]
cantidades = [18, 22, 3]

pedido = Pedido(productos, cantidades)

print('Total pedido: ' + str(pedido.total_pedido()))
pedido.mostrar_pedido()