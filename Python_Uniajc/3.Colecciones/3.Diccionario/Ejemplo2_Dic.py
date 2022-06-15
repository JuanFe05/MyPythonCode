from sympy import true


persona = {} # Diccionario vacio

acceder = True

while acceder:
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Apellidos: ")
    habilidades = input("Cual son tus habilidades: ")
    
    persona['nombre'] = nombre
    persona['apellido'] = apellido
    persona['habilidades'] = habilidades

    repetir = input("Desea agregar otra persona (S/N): ")
    
    if repetir.lower() == 'n':
        acceder = False

for clave in persona.keys():
    print(clave)

for clave, valor in persona.items():
    print(clave, valor)  # de esta manera obtenemos las claves y los valores impresos
