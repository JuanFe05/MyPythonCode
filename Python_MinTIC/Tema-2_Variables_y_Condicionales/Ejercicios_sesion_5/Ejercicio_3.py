n1 = float(input("Ingrese un número: "))
n2 = float(input("Ingrese otro número: "))
opcion = int(input("Seleccione: \n 1 -> Sumar\n 2 -> Multiplicar\n 3 -> Restar\n 4 -> Dividir: "))

resultado = 0

if opcion == 1:
    resultado = n1 + n2
    print(f"El resultado es: {resultado}")

elif opcion == 2:
    resultado = n1 * n2
    print(f"El resultado es: {resultado}")

elif opcion == 3:
    resultado = n1 - n2
    print(f"El resultado es: {resultado}")

elif opcion == 4:
    resultado = n1 / n2
    print(f"El resultado es: {resultado}")

else:
    print("Elige un opción verdadera.")