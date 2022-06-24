temperaturas = [[24, 19, 34, 30, 37, 42, 36], [31, 20, 26, 24, 30, 24, 42], [43, 36, 31, 44, 44, 35, 32]]
profundidades = [[71, 59, 100, 103, 95, 38, 62], [64, 54, 61, 40, 22, 77, 103], [39, 27, 66, 46, 63, 26, 46]]


nA = mgA = mdA = sA = 0
conteoZonas = []

for i in range(len(temperaturas)):

    nada_apto = marginalmente_apto = moderadamente_apto = sumamente_apto = 0

    for j in range(len(temperaturas[i])):

        temperatura = temperaturas[i][j]
        profundidad = profundidades[i][j]
        no_apto = mar_apto = mod_apto = sum_apto = 0

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




print(nA, mgA, mdA, sA)
print(conteoZonas)