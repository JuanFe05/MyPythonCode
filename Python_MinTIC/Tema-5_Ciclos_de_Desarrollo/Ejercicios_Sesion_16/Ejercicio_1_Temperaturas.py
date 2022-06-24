import random

columnas = 7
filas = 5

#Matriz que almacena las temperaturas.
matrizMes = [random.choices(range(7, 38), k=columnas) for fil in range(filas)]

# Creación del calendario del més
print("LUN MAR MIE JUV VIR SAB DOM")
for semanas in range(filas):

    if semanas == filas - 1:
        diaMes = 3
    else:
        diaMes = 7

    for dias in range(diaMes):
        if matrizMes[semanas][dias] < 10:
            print ("",matrizMes[semanas][dias], end="° ")
        else:
            print (matrizMes[semanas][dias], end="° ")
    print()
print()

########################################################################################################################
diasMes = {'1':'LUNES', '2':'MARTES', '3':'MIÉRCOLES', '4':'JUEVES', '5':'VIERNES', '6':'SÁBADO', '7':'DOMINGO'}
maxTempMes = matrizMes[0][0]
maxTempSemMes = 0
maxTempDiaMes = 1
#Temperatura mayor del més
maximo = 1
indice_maximo = ()
indice_maximo_fila = 0
indice_maximo_colu = 0

for semanas in range(filas):

    #Temperatura más alta de la semana y su día
    maxTempSemana = matrizMes[semanas][0]
    maxTempDia = 1
    #Temperatura más baja de la semana y su día
    minTempSemana = matrizMes[semanas][0]
    minTempDia = 1
    #Variable Suma de las temperaturas
    sumTemperaturas = 0

    if semanas == filas - 1:
        diaMes = 3
    else:
        diaMes = 7

    for dias in range(diaMes):
        #Temperatura mayor en la semana
        if matrizMes[semanas][dias] > maxTempSemana:
            maxTempSemana = matrizMes[semanas][dias]
            maxTempDia = dias + 1

        #Temperatura menor en la semana
        elif matrizMes[semanas][dias] < minTempSemana:
            minTempSemana = matrizMes[semanas][dias]
            minTempDia = dias + 1

        sumTemperaturas = sumTemperaturas + matrizMes[semanas][dias]

    #Temperatura promedio de la semana.
    if semanas == filas - 1:
        promTempSemana = sumTemperaturas / 3
    else:
        promTempSemana = sumTemperaturas / columnas


    print(f"En la semana {semanas + 1} la mayor temperatura es de {maxTempSemana} del día {diasMes[str(maxTempDia)]}")
    print(f"En la semana {semanas + 1} la menor temperatura es de {minTempSemana} del día {diasMes[str(minTempDia)]}")
    print(f"Promedio temperatura semanal {round(promTempSemana, 2)}")
    print()

#Temperatura mayor del més y su día
for dias in range(filas):
    for semanas in range(columnas):
        if matrizMes[dias][semanas] > maximo:
            maximo = matrizMes[dias][semanas]
            indice_maximo_fila = dias + 1
            indice_maximo_colu = semanas + 1

print(f"La temperatura máxima del mes es: {maximo}° del día {diasMes[str(indice_maximo_colu)]} en la semana({indice_maximo_fila})")