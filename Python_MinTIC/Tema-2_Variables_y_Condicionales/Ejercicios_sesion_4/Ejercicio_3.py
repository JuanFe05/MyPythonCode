total_pag = int(input("Ingrese el valor a pagar: "))
metodo = int(input("Ingrese el método de pago: \n 1 = efectivo \n 2 = credito -> "))

total = 0

if metodo == 1:
    total = total_pag - (total_pag * 0.10)
    print(f"Total pagar: {total}")

elif metodo == 2:
    total = total_pag + (total_pag * 0.07)
    print(f"Total pagar: {total}")

else:
    print("DEBE INGRESAR UN METODO DE PAGO")