numero = int(input("Ingrese un número: "))
numInverso = 0

try:
    while numero > 0:
        residuo = numero % 10
        numInverso = (numInverso * 10) + residuo
        numero //= 10
    print(f"El inverso del número ingresado es: {numInverso}")

except ValueError:
    print("Ese número no es valido. Inténtalo de nevo !")