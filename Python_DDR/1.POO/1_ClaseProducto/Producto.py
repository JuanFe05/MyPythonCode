class Producto:
    
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo  # Atributo privado (__)
        self.__nombre = nombre
        self.__precio = precio
        
    @property # Indica que es un get
    def codigo(self):
        return self.__codigo
    
    @codigo.setter # Indica que es un set
    def codigo(self, valor):
        self.__codigo = valor
        
    @property # Indica que es un get
    def nombre(self):
        return self.__nombre
    
    @nombre.setter # Indica que es un set
    def nombre(self, valor):
        self.__nombre = valor
        
    @property # Indica que es un get
    def precio(self):
        return self.__precio
    
    @precio.setter # Indica que es un set
    def precio(self, valor):
        self.__precio = valor
        
    # Método propio
    def calcularTotal(self, unidades):
        return self.__precio * unidades
        
    # toString
    def __str__(self):
        return 'Código: ' + str(self.__codigo) + ' Nombre: ' + self.__nombre + ' Precio: ' + str(self.__precio)
    
producto1 = Producto(1, 'Computador', 2500000)
producto2 = Producto(2, 'Lavadora', 1500000)
producto3 = Producto(3, 'Nevera', 3650000)

print(producto1.nombre)
print(producto2.precio)
print(producto3)

print(producto1.calcularTotal(5))
print(producto2.calcularTotal(10))
print(producto3.calcularTotal(28))