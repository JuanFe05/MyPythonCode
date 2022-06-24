cantidad    = int(input("Ingrese la cantidad que vendió: "))
precio_unid = int(input("Ingrese el precio por unidad vendida: "))

calcular = total_com = total = 0

if cantidad >= 5000 and cantidad <= 9999:
    calcular = cantidad * precio_unid
    total_com = (0.05 * calcular)
    total = calcular + total_com
    print(f"La comisión ganada es {total_com} para un total de: {total}")

elif cantidad > 9999:
    calcular = cantidad * precio_unid
    total_com = (0.1 * calcular)
    total = calcular + total_com
    print(f"La comisión ganada es {total_com} para un total de: {total}")

else:
    calcular = cantidad * precio_unid
    total = calcular + total_com
    print(f"La comisión ganada es {total_com} para un total de: {total}")
