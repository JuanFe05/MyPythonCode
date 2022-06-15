from Personas import Persona

persona1 = Persona("Juan", "Herman", 23)
persona1.aggHabilidad("PYTHON")
persona1.aggHabilidad("JAVA")
persona1.aggHabilidad("REACT")

print(persona1.datosPersona())
print(*persona1.habilidades)    # El * me permite imprimir la lista de forma normal
