from Productos import Producto

class Pedido:
    
    # Constructor
    def __init__ (self):
        self.__productos = []
        self.__cantidades = []
        
    # Métodos propios
    def agregar_producto(self, producto, cantidad):
        if not isinstance(producto, Producto):
            raise Exception('agregar_producto: producto debe ser de la clase producto')
        
        if not isinstance(cantidad, int):
            raise Exception('agregar_producto: cantidad debe ser un número')
        
        if cantidad <= 0:
            raise Exception('agregar_producto: cantidad deber ser mayor a cero')
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            self.__cantidades[indice] = self.__cantidades[indice] + cantidad
            
        else:
            self.__productos.append(producto)
            self.__cantidades.append(cantidad)
    
    def eliminar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise Exception('eliminar_producto: producto debe ser de la clase producto')
        
        if producto in self.__productos:
            indice = self.__productos.index(producto)
            del self.__productos[indice]
            del self.__cantidades[indice]
            
        else:
            raise Exception('eliminar_producto: producto no existe')
    
    def total_pedido(self):
        total = 0
        
        for (producto, cantidad) in zip(self.__productos, self.__cantidades):
            total = total + producto.calcularTotal(cantidad)
            
        return total
    
    def mostrar_pedido(self):
        for (producto, cantidad) in zip(self.__productos, self.__cantidades):
            print('Producto -> (' , producto , ') Cantidad: ' + str(cantidad))