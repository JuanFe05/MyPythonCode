filas = int(input("Número de Filas: "))
columnas = int(input("Número de Columnas: "))

matriz = []

for i in range(filas):
    matriz.append([])
    for j in range(columnas):
        valor = float(input(f"Fila {i + 1}, Columna {j + 1}: "))
        matriz[i].append(valor)

print()

for fila in matriz:
    print("[", end=" ")
    for elemento in fila:
        print(f"{elemento:8.2f}", end=" ")
    print("]")

print()