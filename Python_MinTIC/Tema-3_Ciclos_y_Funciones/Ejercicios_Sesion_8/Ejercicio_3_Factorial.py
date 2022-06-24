respuesta = "s"

while respuesta.lower() == "s":
    num = int(input("Ingrese el número al cual desea hacerle el factorial: "))

    factorial = 1

    while num > 1:
        factorial = factorial * num
        num -= 1
        print(f"{factorial}")

    respuesta = input("Desea continuar: S/N: ")

print("Programa finalizado")