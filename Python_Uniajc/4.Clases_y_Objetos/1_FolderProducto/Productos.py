class Producto:

    # Constructor
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo # __codigo = el doble (__) indica un atributo privado.
        self.__nombre = nombre # __nombre = el doble (__) indica un atributo privado.
        self.__precio = precio # __precio = el doble (__) indica un atributo privado.

    #property() es una función integrada en Python que permite interceptar la lectura, escritura y borrado de atributos.

    #Get codigo
    @property
    def getCodigo(self):
        return self.__codigo

    #Set codigo
    @getCodigo.setter
    def setCodigo(self, valor):
        self.__codigo = valor

    #Get nombre
    @property
    def nombre(self):
        return self.__nombre

    #Set nombre
    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    #Get precio
    @property
    def precio(self):
        return self.__precio

    #Set precio
    @precio.setter
    def precio(self, valor):
        self.__precio = valor

    def calcular_total(self, cantidadUnidades):
        return self.precio * cantidadUnidades

    # Parecido al toString de java.
    def __str__(self):
        return 'Código: ' + str(self.__codigo) + ' Nombre: ' + self.__nombre + ' Precio: ' + str(self.__precio)
