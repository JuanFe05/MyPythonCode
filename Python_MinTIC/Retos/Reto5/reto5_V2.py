import csv

conteoCiudades = []
aptitudCiudad = []



with open('data.csv', 'r', encoding='utf-8-sig') as datosCiudades:
    datos = datosCiudades.read().splitlines()
    datos.pop(0)

    for i in datos:
        dato = i.split(',')

        conteoCiudades.append([int(dato[3]), int(dato[5]), dato[6]])



datosCiudades.close()

temperaturas = []
profundidades = []
# aptitud = []

for elementos in conteoCiudades:
    temperaturas.append(elementos[0])
    profundidades.append(elementos[1])
    # aptitud.append(elementos[2])

# print("Temp: ", len(temperaturas), " Prof: ", len(profundidades))
# print("Temp: ", sum(temperaturas), " Prof: ", sum(profundidades))
# print(aptitud)

no_apto = marginalmente_apto = moderadamente_apto = sumamente_apto = 0

for i in aptitudCiudad:

    if i == 'no apto':
        no_apto += 1

    elif i == 'marginalmente apto':
        marginalmente_apto += 1

    elif i == 'moderadamente apto':
        moderadamente_apto += 1

    elif i == 'sumamente apto':
        sumamente_apto += 1

print(no_apto, marginalmente_apto, moderadamente_apto, sumamente_apto)

"""Promedio"""
print("{0:.2f}".format(sum(temperaturas)/len(temperaturas)), "{0:.2f}".format(sum(profundidades)/len(profundidades)))
# print(round((sum(temperaturas))/len(temperaturas), 2), round(sum(profundidades)/len(profundidades), 2))

"""Minimo y maximo"""
# print(min(temp), min(prof))
# print(max(temp), max(prof))