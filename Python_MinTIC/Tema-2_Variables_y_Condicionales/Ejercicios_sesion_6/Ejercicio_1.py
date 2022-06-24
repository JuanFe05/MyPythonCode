import math

n = abs(int(input("Ingresa un número de 4 DÍGITOS: ")))

if n >= 1000 and n <= 9999:
    n1 = math.trunc((n / 1000) % 10)
    n2 = math.trunc((n / 100) % 10)
    n3 = math.trunc((n / 10) % 10)
    n4 = math.trunc((n % 10) % 10)

    number = max(n1,n2,n3,n4)

    if number % 2 == 0:
        print(f"EL NÚMERO MAYOR ES: {number} Y ES PAR")

    else:
        print(f"EL NÚMERO MAYOR ES: {number} Y ES IMPAR")

else:
    print("DEBE INGRESAR UN NUMERO DE 4 DÍGITOS")