print("Tipos de triángulos según sus lados")

lado_1 = int(input("Ingrese el primer lado: "))
lado_2 = int(input("Ingrese el segundo lado: "))
lado_3 = int(input("Ingrese el tercer lado: "))

if lado_1 == lado_2 and lado_1 == lado_3:
    print("Triángulo equilátero, tiene todos sus lados iguales.")

elif lado_1 != lado_2 and lado_1 != lado_3:
    print("Triángulo escaleno, los tres lados son desiguales.")

else:
    print("Triángulo isósceles, tiene dos lados iguales.")