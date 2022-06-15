num = 0
cantNum = 0

while -10 <= num <= 10:
    num = int(input("Número: "))

    if num == 0:
        print("Error, el cero no tiene opuesto")
        break

    print(f"Opuesto de {num} es {num * -1}")
    cantNum += 1

print(f"La cantidad de números ingresados es de: {cantNum}")

#########################################################
""" continuar = "s"

while (continuar.lower() == "s"):
    tabla = int(input("Ingrese un Número para formar la tabla de multiplicar: "))
    i = 0
    while (i <= 10):
        print(f"{tabla} x {i} = {i * tabla}")
        i += 1

    continuar = input("Desa continuar S/N: ")

print("Programa finalizado") """
