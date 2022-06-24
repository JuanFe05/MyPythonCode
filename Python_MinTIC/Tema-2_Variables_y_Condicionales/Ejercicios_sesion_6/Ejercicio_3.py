import math

n1 = abs(int(input("Ingresa un número de 3 DÍGITOS: ")))

if n1 >= 100 and n1 <= 999:
    n_1 = math.trunc((n1 / 100) % 10)
    n_2 = math.trunc((n1 / 10) % 10)
    n_3 = math.trunc((n1 % 10) % 10)
    number = 0

    if n_1 >= n_2 and n1 >= n_3 and n_2 >= n_3:
        number = str(n_1) + str(n_2) + str(n_3)

    elif n_2 >= n_1 and n_2 >= n_3 and n_3 >= n_1:
        number = str(n_2) + str(n_3) + str(n_1)

    elif n_3 >= n_1 and n_3 >= n_2 and n_2 >= n_1:
        number = str(n_3) + str(n_2) + str(n_1)

    print(number)

else:
    print("EL NÚMERO NO ES DE TRES DÍGITOS")
