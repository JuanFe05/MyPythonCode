conteoZonas = [[1, 2, 4, 0],
               [5, 1, 1, 0],
               [2, 3, 2, 0]]

menorF = []
mayorF = []

for i in range(len(conteoZonas)):

    maxTempSemana = conteoZonas[i][0]
    maxTempDia = 1

    minTempSemana = conteoZonas[i][1]
    minTempDia = 1

    for j in range(len(conteoZonas[i])):

        if conteoZonas[i][j] >= maxTempSemana:
            maxTempSemana = conteoZonas[i][j]
            maxTempDia = j + 1

        elif conteoZonas[i][j] <= minTempSemana and conteoZonas[i][j] != 0:
            minTempSemana = conteoZonas[i][j]
            minTempDia = j + 1



    # mayor repetido por zona
    if maxTempDia == 1:
        mayorF.append("no apto")
    elif maxTempDia == 2:
        mayorF.append("marginalmente apto")
    elif maxTempDia == 3:
        mayorF.append("moderadamente apto")
    elif maxTempDia == 4:
        mayorF.append("sumamente apto")

    # menor repetido por zona
    if minTempDia == 1:
        menorF.append("no apto")
    elif minTempDia == 2:
        menorF.append("marginalmente apto")
    elif minTempDia == 3:
        menorF.append("moderadamente apto")
    elif minTempDia == 4:
        menorF.append("sumamente apto")



    # print("menor", maxTempSemana, maxTempDia, mayorF)
    # print("menor", minTempSemana, minTempDia, menorF)
    # print()
    # print(maxTempSemana, frase)
    # print([mayorF])




# print("Mayor: ", mayorF, end=", ")
# print()
# print("Menor: ", menorF, end=", ")

print((','.join(mayorF)))
print((','.join(menorF)))

# print("mayor", maxTempSemana, maxTempDia, mayorF)
print()
print(conteoZonas)



# for x in range(len(mayorF)):
#     print(mayorF, end=" ")

