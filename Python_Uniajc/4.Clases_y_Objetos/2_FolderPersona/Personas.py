class Persona:
    
    # Constructor
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre        # Atributo público
        self.apellido = apellido    # Atributo público
        self.edad = edad            # Atributo público
        self.habilidades = []       # Lista pública
        
    # Métodos propios
    def datosPersona(self):
        return f'Hola {self.nombre} {self.apellido} tu edad es de {self.edad} años'
    
    def aggHabilidad(self, habilidadesPersona):
        self.habilidades.append(habilidadesPersona)
