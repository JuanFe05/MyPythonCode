#Compresion  de matrices

import random

fil = 3
col = 3

a = [[random.randint(1, 100) for i in range(fil)] for j in range(col)]

for filas in range(fil):
    for columnas in range(col):
        if a[filas][columnas] < 10:
            print ("", a[filas][columnas], end=" ")
        else:
            print (a[filas][columnas], end=" ")
    print()