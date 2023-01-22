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