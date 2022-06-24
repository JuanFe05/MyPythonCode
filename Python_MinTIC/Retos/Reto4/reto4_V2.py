nA = mgA = mdA = sA = 0
conteoZonas = []
menorF = []
mayorF = []

n_zonas = int(input("N° zonas: "))

while n_zonas <= 0:
    n_zonas = int(input("N° zonas: "))

temperaturas = [[int(j) for j in input("Temperaturas: ").split()] for i in range(n_zonas)]

profundidades = [[int(j) for j in input("Profundidades: ").split()] for i in range(n_zonas)]

for i in range(len(temperaturas)):

    nada_apto = marginalmente_apto = moderadamente_apto = sumamente_apto = 0

    for j in range(len(temperaturas[i])):

        no_apto = mar_apto = mod_apto = sum_apto = 0
        temperatura = temperaturas[i][j]
        profundidad = profundidades[i][j]

        """ Validando Temperaturas """
        if (temperatura > 24 and temperatura <= 28):
            sum_apto += 1
        elif ((temperatura > 28 and temperatura <= 30) or (temperatura > 20 and temperatura <= 24)):
            mod_apto += 1
        elif ((temperatura > 30 and temperatura <= 32) or (temperatura >= 18 and temperatura <= 20)):
            mar_apto += 1
        else:
            no_apto += 1

        """ Validando Profundidades """
        if (profundidad > 100):
            sum_apto += 1
        elif (profundidad > 50 and profundidad <= 100):
            mod_apto += 1
        elif (profundidad >= 25 and profundidad <= 50):
            mar_apto += 1
        else:
            no_apto += 1

        """ Validando Valores Completamente """
        if (no_apto > 0):
            nada_apto += 1
            nA += 1
        elif (mar_apto > 0):
            marginalmente_apto += 1
            mgA += 1
        elif (mod_apto > 0):
            moderadamente_apto += 1
            mdA += 1
        else:
            sumamente_apto += 1
            sA += 1

    conteoZonas.append([nada_apto, marginalmente_apto, moderadamente_apto, sumamente_apto])

########################################################################################################################
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

########################################################################################################################
print(nA, mgA, mdA, sA)
print((','.join(mayorF)))
print((','.join(menorF)))
print()
print(conteoZonas, end="\n")