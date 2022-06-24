import csv

temperaturas = []
profundidades = []
aptitudCiudad = []

nombreCiudad = input()

with open('data.csv', 'r', encoding='utf-8-sig') as datosCiudades:
    datos = csv.DictReader(datosCiudades)

    try:
        for filas in datos:
            if filas['capital'] == nombreCiudad:
                aptitudCiudad.append(filas['aptitud'])
                temperaturas.append(int(filas['temperatura_media_anual']))
                profundidades.append(int(filas['profundidad_efectiva_suelo']))
    except:
        print("Error")

datosCiudades.close()

no_apto = marginalmente_apto = moderadamente_apto = sumamente_apto = 0
resultado = []

for i in aptitudCiudad:

    if i == 'no apto':
        no_apto += 1
    elif i == 'marginalmente apto':
        marginalmente_apto += 1
    elif i == 'moderadamente apto':
        moderadamente_apto += 1
    elif i == 'sumamente apto':
        sumamente_apto += 1

resultado.append(["no apto", no_apto])
resultado.append(["marginalmente apto", marginalmente_apto])
resultado.append(["moderadamente apto", moderadamente_apto])
resultado.append(["sumamente apto", sumamente_apto])

try:
    print(round(sum(temperaturas)/len(temperaturas), 2), round(sum(profundidades)/len(profundidades), 2))
    print(min(temperaturas), min(profundidades))
    print(max(temperaturas), max(profundidades))

    for i in range(len(resultado)):
        for j in range(len(resultado[i])):
            print(resultado[i][j], end=' ')
        print()

except:
        print("Fin del programa")