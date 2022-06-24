import math

numero = abs(int(input("Ingresa un número: ")))

i = 0

while numero >= 1:
    numero = math.trunc(numero / 10)
    i += 1

print(f"El número tiene: {i} dígitos")