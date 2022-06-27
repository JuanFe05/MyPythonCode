from Productos import Producto

class Pedido:
    
    # Constructor
    def __init__ (self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades
        
    # Métodos propios
    def total_pedido(self):
        total = 0
        
        for (producto, cantidad) in zip(self.__productos, self.__cantidades):
            total = total + producto.calcularTotal(cantidad)
            
        return total
    
    def mostrar_pedido(self):
        for (producto, cantidad) in zip(self.__productos, self.__cantidades):
            print('Producto -> (' , producto , ') Cantidad: ' + str(cantidad))