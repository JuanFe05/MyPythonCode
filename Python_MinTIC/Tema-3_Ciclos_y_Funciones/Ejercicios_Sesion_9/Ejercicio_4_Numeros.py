lect = int(input("Ingrese cuantos número desea leer: "))

positivos = negativos = neutro = 0

for i in range(lect):
    num = float(input("Número: "))

    if num == 0:
        neutro += 1

    elif num < 0:
        negativos += 1

    else:
        positivos += 1

print(f"Hay {positivos} Positivos, {negativos} Negativos y {neutro} Neutros")