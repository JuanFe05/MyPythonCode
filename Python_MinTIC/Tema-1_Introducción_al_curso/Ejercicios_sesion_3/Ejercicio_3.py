print("App notas")

nombre = input("¿Cual es tu nombre?: ")
nota_1 = int(input("Ingresa la nota número 1: "))
nota_2 = int(input("Ingresa la nota número 2: "))
nota_3 = int(input("Ingresa la nota número 3: "))

promedio_notas = (nota_1 + nota_2 + nota_3 ) / 3

if promedio_notas < 3:
    print(f"REPROBADO, TU NOTA ES: {promedio_notas}")

elif promedio_notas >= 3 and promedio_notas <= 4:
    print(f"APROBADO, TU NOTA ES: {promedio_notas}")

elif promedio_notas > 4:
    print(f"EXCELENTE, APROBADO, TU NOTA ES: {promedio_notas}")