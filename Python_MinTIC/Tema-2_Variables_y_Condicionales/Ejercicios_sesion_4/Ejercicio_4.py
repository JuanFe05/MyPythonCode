juan = int(input("Juan, ingresa tu edad: "))
pedro = int(input("Pedro, ingresa tu edad: "))

sum_edades = (juan + pedro) % 2

if juan > 30 or pedro > 50:
    simon = input("Simón tiene nietos: y = si , n = no: ")

    if simon.lower() == "y" and sum_edades == 0:
        print("TIENE ACCESO")

    else:
        print("NO TIENE ACCESO")

else:
    print("NO TIENE ACCESO")