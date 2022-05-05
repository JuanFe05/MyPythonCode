########################################################

#Adición de elementos a una lista

""" lista = list()
lista.append('Hola')

frutas = ['Banano', 'Naranja', 'Mango', 'Limón']
frutas.append('Sandia')
print(frutas)

frutas.append('Manzana')
print(frutas)
"""
########################################################

# Eliminación de elementos de una lista

""" paises = ['Colombia', 'Chile', 'Brasil', 'Argentina']
paises.remove('Chile')
print(paises)

paises.pop(0) # pop, elimina por indices
print(paises)

del paises[1]
print(paises) """

########################################################

""" # Copiar una lista
paises = ['Colombia', 'Chile', 'Brasil', 'Argentina']
paises_copia = paises.copy()
print(paises_copia) """

########################################################

# unir listas

""" numerosPositivos = [1, 2, 25, 63, 88]
numerosNegativos = [-99, -92, -125, -4, -16]

numeros = numerosPositivos + numerosNegativos
print(*numeros) """

########################################################

# Encontrar el índice de un artículo

numeros = [1, 1, 1, 2, 2, 2, 68, 40, 2 ,4 ,6 ,6]

print(numeros.index(1)) # 0
print(numeros.count(1)) # Cuenta el numero de veces que aparece el 1
