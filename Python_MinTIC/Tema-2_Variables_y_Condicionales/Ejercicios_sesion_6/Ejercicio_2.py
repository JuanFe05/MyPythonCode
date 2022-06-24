import math

n1 = abs(int(input("Ingresa un número de 3 DÍGITOS: ")))
n2 = abs(int(input("Ingresa otro número de 3 DÍGITOS: ")))

if n1 >= 100 and n1 <= 999 and n2 >= 100 and n2 <= 999:
    n_1 = math.trunc((n1 / 100) % 10)
    n_2 = math.trunc((n1 / 10) % 10)
    n_3 = math.trunc((n1 % 10) % 10)
    #################################
    n_4 = math.trunc((n2 / 100) % 10)
    n_5 = math.trunc((n2 / 10) % 10)
    n_6 = math.trunc((n2 % 10) % 10)

    number1 = max(n_1, n_2, n_3)
    number2 = min(n_4, n_5, n_6)

    print("El número combinado es: " + str(number1) + str(number2))

else:
    print("LOS NÚMEROS NO SON DE TRES DÍGITOS")





