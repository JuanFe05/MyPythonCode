numero = int(input("Ingrese un número: "))

if numero > -9 and numero < 9:
    print(f"El numero {numero} es de 1 cifra")

elif numero > -99 and numero < 99:
    print(f"El numero {numero} es de 2 cifras")

elif numero > -999 and numero < 999:
    print(f"El numero {numero} es de 3 cifras")

else:
    print(f"ERROR NÚMERO {numero} ES MAYOR A 3 CIFRAS")