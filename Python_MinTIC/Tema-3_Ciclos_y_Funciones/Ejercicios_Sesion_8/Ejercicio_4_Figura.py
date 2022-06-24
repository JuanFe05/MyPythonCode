respuesta = "s"

while respuesta.lower() == "s":
    numero = int(input("Ingrese un número para formar una figura: "))

    espacios = 0
    caracteres = numero

    while espacios <= (numero - 1):
        print("*" * caracteres, (" " * espacios))
        espacios += 1
        caracteres -= 1

    respuesta = input("Desea continuar: S/N: ")

print("Programa finalizado")