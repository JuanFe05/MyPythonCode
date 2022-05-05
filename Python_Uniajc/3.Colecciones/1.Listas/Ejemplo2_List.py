# Las listas pueden tener elementos de diferentes tipos de datos

Lista = ['Juan Manuel', 20, True, {'pais': 'Colombia', 'ciudad': 'Palmira'}]

########################################################

# Acceder a los elementos de la lista mediante la indexación
frutas = ['Banano', 'Naranja', 'Mango', 'Limón', 'Sandia', 'Manzana']

""" fruta1 = frutas[0]
print(fruta1)

fruta1_otraVez = frutas[-4]
print(fruta1_otraVez)

primera_fruta, segunda_fruta, tercera_fruta, *demas_frutas = frutas
print(primera_fruta)    # Banano
print(segunda_fruta)    # Naranja
print(tercera_fruta)    # Mango
print(demas_frutas)     # ['Limón','Sandia','Manzana'] """

# tambien puedo imprimir desde cierta posicion.
""" print(frutas[1:3]) """

# tambien puedo imprimir de dos en dos o la cantidad que yo desee.
""" print(frutas[::2]) """

# tambien puedo modificar mi lista.
frutas[0] = 'Pera'
print(frutas)