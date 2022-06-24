print("Test de capacitación")

cant_preguntas = int(input("Ingrese la cantidad total de preguntas realizadas: "))
cant_acertadas = int(input("Ingrese la cantidad de preguntas acertadas: "))

porcentaje = (cant_acertadas * 100) / cant_preguntas

if porcentaje >= 90:
    print(f"NIVEL MÁXIMO, tu porcentaje es: {porcentaje}")

elif porcentaje >= 75 and porcentaje < 90:
    print(f"NIVEL MEDIO, tu porcentaje es: {porcentaje}")

elif porcentaje >= 50 and porcentaje < 75:
    print(f"NIVEL REGULAR, tu porcentaje es: {porcentaje}")

elif porcentaje < 50:
    print(f"FUERA DE NIVEL, tu porcentaje es: {porcentaje}")

else:
    print("INGRESE VALORES VÁLIDOS")