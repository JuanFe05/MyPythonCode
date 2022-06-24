edad = int(input("Ingrese su edad: "))

if edad < 0:
    print("NO PUEDE INGRESAR EDAD NEGATIVA")

elif edad < 18:
    print("USTED ES MENOR DE EDAD")

else:
    print("USTED ES MAYOR DE EDAD")