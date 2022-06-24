def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if(lista[i]>lista[j]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print(lista)

V = [9, 7, 6, 5, 4, 3, 11, 8, 1, 2]
print(V)
ordenar(V)