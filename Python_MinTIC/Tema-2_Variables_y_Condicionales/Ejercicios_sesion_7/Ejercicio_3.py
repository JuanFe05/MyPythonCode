numero = int(input("Ingresa un número pósitivo: "))

veces = 0
acumulado = 0

while numero != -1:
    veces += 1
    acumulado += numero
    numero = int(input("Ingresa un número pósitivo: "))

if veces == 0:
    print("El usuario digitó -1")

else:
    print(f"El promedio es {acumulado/veces}")