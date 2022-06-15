#Un diccionario es una colección de tipos de datos no ordenados, modificables (mutables) emparejados (clave: valor).

########################################################

dicc_vacio = {}
dicc = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}

########################################################

persona = {
    'nombres': 'Juan Felipe',
    'apellidos': 'Herman',
    'edad': 23,
    'pais': 'Colombia',
    'casado': False,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'direccion': {
        'calle': 'carrera 11',
        'barrio': 'La Cabaña'
    }
}

# Imprime la longitud del diccionario
print(len(persona))

# accede a los valores diccionario
print(persona['nombres']) 
print(persona['direccion'])

print(persona.get('habilidades'))

# Adición de elementos a un diccionario
persona['ciudad'] = 'Florida'
persona['habilidades'].append('Java')

# Modificar elementos 
persona['direccion'] = 'carrera 12'

# imprime las claves
claves = persona.keys()
print(claves)

# copiar diccionario
persona_copia = persona.copy()
print(persona_copia)

# borrar diccionario
del persona_copia
