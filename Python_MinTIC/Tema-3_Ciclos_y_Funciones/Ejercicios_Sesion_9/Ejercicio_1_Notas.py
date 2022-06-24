n = int(input("Ingrese el número de notas: "))

sum = 0

for c in range(n):
    nota = float(input("Nota: "))
    sum += nota
    c += 1

prom = sum / n
print(prom)