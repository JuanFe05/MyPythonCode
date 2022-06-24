import csv

file = open("D:/Roymer/MisionTIC2022/Sesiones/Sesion20/archivoClientesEntrega.csv", "r", encoding="utf-8-sig")
lector = csv.reader(file)

encabezado_original = next(lector)
nuevo_encabezado = [encabezado_original[0], "Número de Camiones"]
camion1 = []
camion2 = []
cliente1 = []
cliente2 = []

for row in lector:

    if row[0] == "Lactocaribe" and row[0] not in cliente1:
        cliente1.append(row[0])
    elif row[0] == "Frigoaves" and row[0] not in cliente2:
        cliente2.append(row[0])

    if row[2] not in camion1 and row[0] == "Lactocaribe":
            camion1.append(row[2])
    if row[2] not in camion2 and row[0] == "Frigoaves":
            camion2.append(row[2])

cliente1.append(len(camion1))
cliente2.append(len(camion2))
contenido = [ cliente1 if i==0 else cliente2 for i in range(2)  ]

# Crear el nuevo CSV
nuevo_csv = open("nuevo_csv.csv", "w", newline="", encoding="utf-8-sig")
escribir = csv.writer(nuevo_csv)
escribir.writerow(nuevo_encabezado)
escribir.writerows(contenido)