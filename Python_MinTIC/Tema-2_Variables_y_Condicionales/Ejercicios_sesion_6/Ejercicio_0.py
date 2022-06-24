n1 = int(input("Ingresa un número: "))
n2 = int(input("Ingresa otro número: "))
n3 = int(input("Ingresa otro número: "))

# Utilizando la función max()
print(f"El número más grande es: {max(n1, n2, n3)}")

if n1 > n2 and n1 > n3 or n1 == n2 or n1 == n3:
    print(f"EL NÚMERO MAYOR ES: {n1}")

elif n2 > n1 and n2 > n3 or n2 == n1 or n2 == n3:
    print(f"EL NÚMERO MAYOR ES: {n2}")

elif n3 > n1 and n3 > n2 or n3 == n2 or n3 == n1:
    print(f"EL NÚMERO MAYOR ES: {n3}")


