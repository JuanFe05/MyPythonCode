a = []
m = 3
n = 2

for filas in range(m): # Filas
    a.append([])
    for columnas in range(n): # Columnas
        a[filas].append(None)

for filas in range(m):
    for columnas in range(n):
        print(a[filas][columnas], end=' ')
    print()