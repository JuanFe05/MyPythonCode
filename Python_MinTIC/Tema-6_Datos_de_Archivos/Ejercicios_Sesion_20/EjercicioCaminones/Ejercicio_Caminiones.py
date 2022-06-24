import csv

nCamionesLactocaribe = []
nCamionesFrigoaves = []

with open('archivoClientesEntrega.csv', 'r', encoding='utf-8-sig') as datosCamiones:
    datos = csv.DictReader(datosCamiones)

    for filas in datos:
        if filas['Cliente'] == 'Lactocaribe':
            nCamionesLactocaribe.append(int(filas['ID del Camión']))

        elif filas['Cliente'] == 'Frigoaves':
            nCamionesFrigoaves.append(int(filas['ID del Camión']))

datosCamiones.close()

repetidosLacto = []
repetidosFrigo = []
resultado = []

for x in nCamionesLactocaribe:
    if x not in repetidosLacto:
        repetidosLacto.append(x)

for x in nCamionesFrigoaves:
    if x not in repetidosFrigo:
        repetidosFrigo.append(x)

resultado.append(["Lactocaribe", len(repetidosLacto)])
resultado.append(["Frigoaves", len(repetidosFrigo)])

encabezado = ['Clientes', 'Numero de Camiones']

with open('numeroDeCamiones.csv', 'w', newline='', encoding='utf-8') as miArchivo:
    writer = csv.writer(miArchivo)
    writer.writerow(encabezado)
    writer.writerows(resultado)

print("Escritura completa")