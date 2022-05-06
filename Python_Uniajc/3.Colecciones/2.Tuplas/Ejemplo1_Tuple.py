# Una tupla es una colección de diferentes tipos de datos ordenados e inmutables (inmutables). Las tuplas se escriben con parentesis, (). Una vez que se crea una tupla, no podemos cambiar sus valores.

########################################################

tupla_vacia = ()
tupla_vacia = tuple()

########################################################

tupla = ('item1', 'item2', 'item3')

########################################################

frutas = ('Pera', 'Manzana', 'Mango', 'Sandia')
print(len(frutas))
print(frutas[0])

frutas2 = ('Pera', 'Manzana', 'Mango', 'Sandia')
del frutas2
print(frutas2)
