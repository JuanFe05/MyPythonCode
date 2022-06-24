val_hora = int(input("Ingrese el valor de la Hora: "))
num_hora_ext = int(input("Ingrese las Horas extras laboradas: "))
tipo_hora = int(input("Ingrese el tipo de hora extra,\n 1 = Diurnas\n 2 = Nocturnas \n -> "))

total_ganado = 0

if tipo_hora == 1:
    total_ganado = val_hora * num_hora_ext

elif tipo_hora == 2:
    total_ganado = (val_hora * num_hora_ext) * 2

print(f"El trabajador laboró {num_hora_ext} horas extras, y ganó en total {total_ganado}")
