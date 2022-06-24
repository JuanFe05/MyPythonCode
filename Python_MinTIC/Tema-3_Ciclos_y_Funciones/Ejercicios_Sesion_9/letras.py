cadena = input("Escribe cualquier cosa: ")

# Método 1, sin índice
for i in range(len(cadena)):
    #print(cadena[i], end=" ")

    if cadena[i] == "a":
        print(f"{cadena} Tiene una a")
        break
