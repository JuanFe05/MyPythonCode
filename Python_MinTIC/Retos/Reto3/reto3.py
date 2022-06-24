temperaturas = []
profundidades = []
tempTotal = []
profTotal = []
nada_apto = marginalmente_apto = moderadamente_apto = sumamente_apto = 0

n_zonas = int(input("numero de zonas: "))

while n_zonas <= 0:
    n_zonas = int(input("numero de zonas: "))

while n_zonas != 0:
    print(f"\nDATOS NUMERO {n_zonas}")

    temperaturas = input().split()
    temperaturas = list(map(float, temperaturas))

    profundidades = input().split()
    profundidades = list(map(float, profundidades))

    sum_apto = mod_apto = mar_apto = no_apto = 0

    promTemp = sum(temperaturas)/len(temperaturas)
    promProf = sum(profundidades)/len(profundidades)

    """ Validando Temperaturas """
    if (promTemp > 24 and promTemp <= 28):
        sum_apto += 1
        
    elif ((promTemp > 28 and promTemp <= 30) or (promTemp > 20 and promTemp <= 24)):
        mod_apto += 1
    
    elif ((promTemp > 30 and promTemp <= 32) or (promTemp >= 18 and promTemp <= 20)):
        mar_apto += 1
    
    else:
        no_apto += 1
        
    """ Validando Porfundidades """
    if ( promProf > 100 ):
        sum_apto += 1

    elif ( promProf > 50 and promProf <= 100 ):
        mod_apto += 1

    elif ( promProf >= 25 and promProf <= 50 ):
        mar_apto += 1

    else:
        no_apto += 1
        
    """ Validando Valores Completamente """
    if (no_apto > 0):
        nada_apto += 1

    elif (mar_apto > 0):
        marginalmente_apto += 1

    elif (mod_apto > 0):
        moderadamente_apto += 1

    else:
        sumamente_apto += 1

    tempTotal.append(promTemp)
    profTotal.append(promProf)

    n_zonas -= 1

##########################################
print()
for i in tempTotal:
    print("{0:.2f}".format(i), end=" ")
print()
for j in profTotal:
    print("{0:.2f}".format(j), end=" ")

print(f"\nsumamente apto {sumamente_apto}")
print(f"moderadamente apto {moderadamente_apto}")
print(f"marginalmente apto {marginalmente_apto}")
print(f"no apto {nada_apto}")