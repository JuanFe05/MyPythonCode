import random

def aleatorio():
    maximo = 1
    minimo = 100
    indice_maximo = ()
    indice_minimo = ()
    matriz = []

    for i in range(5):
        matriz.append([])
        for j in range(10):
            elementos = random.randrange(1,100)
            matriz[i].append(elementos)

            if elementos > maximo:
                maximo = elementos
                indice_maximo = (i,j)

            if elementos < minimo:
                minimo = elementos
                indice_minimo = (i,j)

    print(matriz)
    print(f"el maximo es: {maximo} y se ubica en: {indice_maximo}")
    print(f"el minimo es: {minimo} y se ubica en: {indice_minimo}")

aleatorio()