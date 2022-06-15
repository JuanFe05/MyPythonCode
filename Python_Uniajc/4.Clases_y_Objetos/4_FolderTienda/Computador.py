class Computador:
    
    # Constructor
    def __init__(self, marca, cantidadMemoria, procesador, sistemaOperativo, precio):
        self.marca = marca
        self.cantidadMemoria = cantidadMemoria
        self.procesador = procesador
        self.sistemaOperativo = sistemaOperativo
        self.precio = precio
        
    def __getattribute__(self, attr):
        return object.__getattribute__(self, attr)
