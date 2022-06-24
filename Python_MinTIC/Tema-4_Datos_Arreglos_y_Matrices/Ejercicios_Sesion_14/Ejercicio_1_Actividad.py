import random

def actividad1():
    filas = int(input("Introduce el número de filas que quieres: "))
    columnas = int(input("Introduce el número de columnas que quieres: "))
    
    matriz = []
    
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(random.randint(1, 100))
            print(matriz[i][j], end=" ")
        print("\n")
        
    index = 0
    
    if len(matriz) == len(matriz[0]):
        for i in range(len(matriz)):
            print(f"- {matriz[index][index]}", end=" ")
            index += 1
    else: 
        print("La matriz no es un cuadrado perfecto!!")
        
actividad1()