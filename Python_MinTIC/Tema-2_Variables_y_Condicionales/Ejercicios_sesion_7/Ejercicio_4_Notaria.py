respuesta = ""
total_parejas = 0

######### NÚMERO DE PAREJAS #########
n_parejas = int(input("Ingrese el número de parejas que desean casarse: "))

while n_parejas <= 0 or n_parejas > 10:
    n_parejas = int(input("Ingrese el número de parejas correcto que desean casarse: "))

while respuesta.lower() != "n" and n_parejas != 0:
    ######### EDAD DE LAS PERSONAS #########
    edad_P1 = int(input("\n• Ingresa la edad de la primera persona: "))
    edad_P2 = int(input("• Ingresa la edad de la Segunda persona: "))

    while edad_P1 <= 0 or edad_P1 > 100 or edad_P2 <= 0 or edad_P2 > 100:

        if edad_P1 <= 0 or edad_P1 > 100:
            edad_P1 = int(input("• Ingresa la edad correcta de la primera persona: "))
        else:
            edad_P2 = int(input("• Ingresa la edad correcta de la segunda persona: "))

    if edad_P1 < 18 or edad_P2 < 18:
        print("No se pueden casar, uno o los dos son menores de edad.")

    ######### ESTADO CIVIL DE LAS PERSONAS #########
    else:
        e_civil = input("¿Son solteros? (S=Si, N=No): ")

        while e_civil.lower() != "s" and e_civil.lower() != "n":
            e_civil = input("• ¿Son solteros? (S=Si, N=No): ")

        if e_civil.lower() == "s":
            print("Se pueden Casar")
        else:
            print("No se pueden Casar")

    ################################################
    respuesta = input("\nDesea continuar ingresando parejas (S/N): ")

    total_parejas += 1
    n_parejas -= 1

print(f"\n-> El total de las parejas entrevistadas es de: {total_parejas}")
print(f"-> El número de parejas por entrevistar de es: {n_parejas}")