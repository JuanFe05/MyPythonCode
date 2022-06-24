conteoZonas = [[7, 0, 0, 0],
               [4, 2, 1, 0],
               [1, 0, 5, 1]]

mayorF = []
menorF = []

for i in range(len(conteoZonas)):

    maxTempSemana = conteoZonas[i][0]
    maxTempDia = 1

    for j in range(len(conteoZonas[i])):

        if conteoZonas[i][j] >= maxTempSemana:
            maxTempSemana = conteoZonas[i][j]
            maxTempDia = j + 1

    # mayor repetido por zona
    if maxTempDia == 1:
        mayorF.append("no apto")
    elif maxTempDia == 2:
        mayorF.append("marginalmente apto")
    elif maxTempDia == 3:
        mayorF.append("moderadamente apto")
    elif maxTempDia == 4:
        mayorF.append("sumamente apto")


for i in range(len(conteoZonas)):

    minTempSemana = conteoZonas[i][0]
    minTempDia = 1

    for j in range(len(conteoZonas[i])):
        if conteoZonas[i][j] <= minTempSemana and conteoZonas[i][j] != 0:
            minTempSemana = conteoZonas[i][j]
            minTempDia = j + 1

    # print(minTempDia)
    print("posicion: ",minTempDia, "numero: ",minTempSemana)

    # menor repetido por zona
    if minTempDia == 1:
        menorF.append("no apto")
    elif minTempDia == 2:
        menorF.append("marginalmente apto")
    elif minTempDia == 3:
        menorF.append("moderadamente apto")
    elif minTempDia == 4:
        menorF.append("sumamente apto")

print((','.join(mayorF)))
print((','.join(menorF)))
print()
print(conteoZonas)