fecha = int(input("Ingresa una año: "))

if fecha % 4 != 0:
    print(f"El año {fecha} no es un año bisiesto.")

elif fecha % 100 == 0 and fecha % 400 != 0:
    print(f"El año {fecha} no es un año bisiesto, porque es multiplo de 100 sin ser multiplo de 400")

elif fecha % 4 == 0 and fecha % 100 != 0:
    print(f"El año {fecha} es un año bisiesto, porque es multiplo de 4 sin ser multiplo de 100")

else:
    print(f"El año {fecha} es un año bisiesto porque es multiplo de 400")