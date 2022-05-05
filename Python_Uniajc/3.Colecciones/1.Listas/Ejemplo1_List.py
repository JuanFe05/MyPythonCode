# Lista: es una colección ordenada y cambiable (modificable). Permite miembros duplicados.

# Cómo crear una lista ?

########################################################

lista1 = [] 

lista1_vacia = []  # esta es una lista vacía, no hay ningún elemento en la lista
print(len(lista1_vacia))  # 0

########################################################

lista2 = list()

lista2_vacia = list()  # esta es una lista vacía, no hay ningún elemento en la lista
print(len(lista2_vacia))  # 0

########################################################

frutas = ['Banano', 'Naranja', 'mango', 'Limón']                     
verduras = ['Yuca', 'Papa', 'Repollo', 'Cebolla', 'Zanahoria']
productos_animales = ['Leche', 'Carne', 'manteca', 'yoghurt']
tecnologias_web = ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
paises = ['Finland', 'Colombia', 'Argentina', 'Suecia', 'USA']

print('Frutas:', frutas)
print('Número de frutas:', len(frutas))

print('Verduras:', verduras)
print('Número de Verduras:', len(verduras))

print('Productos Animales:', productos_animales)
print('Número de productos Animales:', len(productos_animales))

print('tecnologías Web:', tecnologias_web)
print('Número de tecnologías Web:', len(tecnologias_web))

print('Paises:', paises)
print('Número de Paises:', len(paises))
