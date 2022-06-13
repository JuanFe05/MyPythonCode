class Tienda:
    
    # Constructor
    def __init__(self, nombre, propietario, identificadorTributario):
        self.nombre = nombre
        self.propietario = propietario
        self.identificadorTributario = identificadorTributario
        self.computadores = []

    # Métodos propios
    def agregarComputador(self, computador):
        self.computadores.append(computador)
        
    # Busca computador
    def buscar(self, key, by="marca"):
        print("{:<5} {:<10} {:<12} {:<24} {:<20} {:<20}".format(
            'Id', 'Marca', 'Memoria', 'Procesador', 'Sistema Operativo', 'Precio'))
        
        for index, computador in enumerate(self.computadores):
            if computador.__getattribute__(by) == key:
                print("{:<5} {:<10} {:<12} {:<24} {:<20} $ {:<20}".format(
                    index, computador.marca, computador.cantidadMemoria, computador.procesador, computador.sistemaOperativo, computador.precio))

    # Elimina computador
    def eliminar(self, key, by="marca"):
        for index, computador in enumerate(self.computadores):
            if computador.__getattribute__(by) == key:
                self.computadores.pop(index)
        
    # Imprime todos los computadores
    def imprimirComputadores(self): 
        print("{:<10} {:<12} {:<24} {:<20} {:<20}".format(
            'Marca', 'Memoria', 'Procesador', 'Sistema Operativo', 'Precio'))
        
        for computador in self.computadores:
            print("{:<10} {:<12} {:<24} {:<20} $ {:<20}".format(
                computador.marca, computador.cantidadMemoria, computador.procesador, computador.sistemaOperativo, computador.precio))

