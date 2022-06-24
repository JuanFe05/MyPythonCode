conteoZonas = [[1, 0, 5, 1],
               [1, 0, 5, 1],
               [1, 0, 5, 1]]

menorF = []

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


print((','.join(menorF)))
print()
print(conteoZonas)