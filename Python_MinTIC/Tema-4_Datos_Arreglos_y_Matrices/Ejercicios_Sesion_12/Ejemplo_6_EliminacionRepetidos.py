""" Eliminar número lista """
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numero = int(input("Número para eliminar 0 al 9: "))

""" Primer Forma """
for i in lista:
    if numero in lista:
        lista.remove(numero)
print(lista)

""" Segunda Forma """
for i in range(len(lista)):
    if lista[i] == numero:
        lista.remove(numero)
print(lista)

""" Tercera Forma, eliminando los hasta los número repetidos """
lista_repetidos = [0, 2, 4, 0, 2, 4, 6, 8, 8, 7, 5]
for i in lista_repetidos:
    if numero in lista_repetidos:
        lista_repetidos.remove(numero)
print(lista_repetidos)

""" Última forma para eliminar """
def eliminar(numerito, listado, encontrado):
    for i in range(len(listado)):
        if listado[i] == numerito:
            listado.remove(numero)
            encontrado=1
            break
    return listado, encontrado


lista_repetidos = [0, 2, 4, 0, 2, 4, 6, 8, 8, 7, 5]
numero = int(input("Otro número para eliminar 0 al 9: "))
t = len(lista_repetidos)
estado = 0
i=0
while (i<=t):
    listado, estado = eliminar(numero, lista_repetidos, estado)
    t = len(listado)
    if t != 0:
        i+=1
    else:
        break
if(estado == 0):
    print("Elemento no encontrado")
print(lista_repetidos)