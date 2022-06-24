continuar = "s"

while (continuar.lower() == "s"):
    tabla = int(input("Ingrese un Número para formar la tabla de multiplicar: "))
    i = 0
    while (i <= 10):
        print(f"{tabla} x {i} = {i * tabla}")
        i += 1

    continuar = input("Desa continuar S/N: ")

print("Programa finalizado")