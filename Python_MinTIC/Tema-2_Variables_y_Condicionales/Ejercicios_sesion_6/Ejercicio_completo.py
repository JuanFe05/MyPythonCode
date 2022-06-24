import math

print("OPCIÓN 1 -> Leer un número de 4 dígitos, mostrar el dígito mayor.\n"
      "OPCIÓN 2 -> Leer dos números de 3 dígitos cada uno\n"
      "OPCIÓN 3 -> Leer un número de 3 dígitos y formar el mayor número posible con sus cifras\n")

option = int(input("INGRESE UNA OPCIÓN: "))

#######################################################################################################################
if option == 1:
    n = abs(int(input("• INGRESE UN NÚMERO DE 4 DÍGITOS: ")))

    if n >= 1000 and n <= 9999:
        n1 = math.trunc((n / 1000) % 10)
        n2 = math.trunc((n / 100) % 10)
        n3 = math.trunc((n / 10) % 10)
        n4 = math.trunc((n % 10) % 10)

        if n1 >= (n2 or n3 or n4):
            if n1 % 2 == 0:
                print(f"EL NÚMERO MAYOR ES: {n1} Y ES PAR")
            else:
                print(f"EL NÚMERO MAYOR ES: {n1} Y ES IMPAR")

        elif n2 >= (n1 or n3 or n4):
            if n2 % 2 == 0:
                print(f"EL NÚMERO MAYOR ES: {n2} Y ES PAR")
            else:
                print(f"EL NÚMERO MAYOR ES: {n2} Y ES IMPAR")

        elif n3 >= (n1 or n2 or n4):
            if n3 % 2 == 0:
                print(f"EL NÚMERO MAYOR ES: {n3} Y ES PAR")
            else:
                print(f"EL NÚMERO MAYOR ES: {n3} Y ES IMPAR")

        elif n4 >= (n1 or n2 or n3):
            if n4 % 2 == 0:
                print(f"EL NÚMERO MAYOR ES: {n4} Y ES PAR")
            else:
                print(f"EL NÚMERO MAYOR ES: {n4} Y ES IMPAR")

    else:
        print("DEBE INGRESAR UN NUMERO DE 4 DÍGITOS")

#######################################################################################################################
elif option == 2:
    n1 = abs(int(input("Ingresa un número de 3 DÍGITOS: ")))
    n2 = abs(int(input("Ingresa otro número de 3 DÍGITOS: ")))

    n_1 = math.trunc((n1 / 100) % 10)
    n_2 = math.trunc((n1 / 10) % 10)
    n_3 = math.trunc((n1 % 10) % 10)
    n_4 = math.trunc((n2 / 100) % 10)
    n_5 = math.trunc((n2 / 10) % 10)
    n_6 = math.trunc((n2 % 10) % 10)
    number1 = number2 = 0

    if n1 >= 100 and n1 <= 999:
        if n_1 >= n_2 and n_1 >= n_3:
            number1 = n_1

        elif n_2 >= n_1 and n_2 >= n_3:
            number1 = n_2

        elif n_3 >= n_1 and n_3 >= n_2:
            number1 = n_3

    ###############################################
    if n2 >= 100 and n2 <= 999:
        if n_4 <= n_5 and n_4 <= n_6:
            number2 = n_4

        elif n_5 <= n_4 and n_5 <= n_6:
            number2 = n_5

        elif n_6 <= n_4 and n_6 <= n_5:
            number2 = n_6

        print(f"El número combinado es: {number1}{number2}")

    else:
        print("LOS NÚMEROS NO SON DE TRES DÍGITOS")

#######################################################################################################################
elif option == 3:
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

#######################################################################################################################
else:
    print("ELIGE UNA OPCIÓN CORRECTA")