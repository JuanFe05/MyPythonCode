class Empleado:
    
    # Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.salarios = []
        
    def addSalarios(self, salariosTrabajador):
        self.salarios.append(salariosTrabajador)