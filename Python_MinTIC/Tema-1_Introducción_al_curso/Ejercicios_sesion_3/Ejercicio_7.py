print("PRGRAMA DE NOTAS")

n1 = float(input("Ingrese la nota número 1: "))
n2 = float(input("Ingrese la nota número 2: "))
n3 = float(input("Ingrese la nota número 3: "))

desc_n1 = (20 * n1) / 100
desc_n2 = (30 * n2) / 100
desc_n3 = (50 * n3) / 100

total_n = desc_n1 + desc_n2 + desc_n3

if total_n >= 3.5:
    print(f"APROBO CON UNA NOTA DE: {total_n}")

elif total_n <= 2.0:
    print(f"PIERDE DERECHO A HABILITAR, NOTA DE: {total_n}")

elif 3.5 > total_n > 2.0:
    print(f"TIENE DERECHO A HABILITAR, NOTA DE: {total_n}")