#len() devuelve la longitud de una cadena de caracteres o el número de elementos de una lista.

numero = abs(int(input("Ingrese un número: ")))

if len(str(numero)) == 1:
    print(f"El número {numero} es de {len(str(numero))} cifra")

elif len(str(numero)) == 2:
    print(f"El número {numero} es de {len(str(numero))} cifras")

elif len(str(numero)) == 3:
    print(f"El número {numero} es de {len(str(numero))} cifras")

else:
    print(f"ERROR NÚMERO {numero} MAYOR A 3 CIFRAS, TIENE {len(str(numero))} CIFRAS")