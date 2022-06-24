num = 0
sum = 0

while -10 <= num <= 10:
    num = int(input("Número: "))

    if num == 0:
        print("Error, el cero no tiene opuesto")
        break

    print(f"Opuesto de {num} es {num * -1}")
    sum += 1

print(f"La suma de los número es: {sum-num}")