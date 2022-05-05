a = 2
b = 15

resultado = a if a > b else b

print(resultado)

##########################################
n1, n2 = 1, 8
temp = (n1 * 2, n2 / 2)[n1 < n2]
print(temp)

##########################################
num = 0

if num >= 0:
    if num == 0:
        print("Cero")
    else:
        print("Número positivo")
else:
    print("Número negativo")

##########################################
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