num = int(input("Ingrese el número al cual desea hacerle el factorial: "))

while num != -1:

    factorial = 1

    for i in range(num):
        factorial *= i + 1

    print(f"{factorial}")
    num = int(input("Ingrese el número al cual desea hacerle el factorial: "))

print("Programa finalizado")