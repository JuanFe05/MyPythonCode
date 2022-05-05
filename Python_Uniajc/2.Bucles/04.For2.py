# Bucles con String

""" lenguaje = 'Python' """

""" for letra in lenguaje:
    print(letra) """

""" for i in range(len(lenguaje)):
    print(lenguaje[i]) """

########################################################

""" numeros = (0, 1, 2, 3, 4, 5) # Tuplas.
for numeros in numeros:
    print(numeros)
"""
########################################################

# Diccionario en python
persona = {
    'nombre': 'Juan',
    'apellido': 'Herman',
    'edad': 23,
    'pais': 'Colombia',
    'habilidades': ['JavaScript', 'React', 'Java', 'MongoDB', 'Python'],
    'direccion': {
        'barrio': 'La Cabaña',
        'codigoPostal': '763560'
    }
}

for clave, valor in persona.items():
    print(clave, valor)  # de esta manera obtenemos las claves y los valores impresos
