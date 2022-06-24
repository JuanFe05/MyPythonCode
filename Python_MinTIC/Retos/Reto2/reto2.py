n_entradas = int(input("numero de entradas: "))

total_temp = contador = total_prof = 0
nada_apto = marginalmente_apto = moderadamente_apto = sumamente_apto = 0

while n_entradas <= 0:
    n_entradas = int(input("numero de entradas: "))

while n_entradas != 0:
    print(f"\nDATOS NUMERO {n_entradas}")
    temperatura = float(input("Temperatura media anual (grados C): "))
    profundidad = float(input("Profundidad efectiva del suelo (cm): "))
    
    sum_apto = mod_apto = mar_apto = no_apto = 0

    """ Validando Temperaturas """
    if (temperatura > 24 and temperatura <= 28):
        sum_apto += 1
        
    elif ((temperatura > 28 and temperatura <= 30) or (temperatura > 20 and temperatura <= 24)):
        mod_apto += 1
    
    elif ((temperatura > 30 and temperatura <= 32) or (temperatura >= 18 and temperatura <= 20)):
        mar_apto += 1
    
    else:
        no_apto += 1
        
    """ Validando Porfundidades """
    if ( profundidad > 100 ):
        sum_apto += 1

    elif ( profundidad > 50 and profundidad <= 100 ):
        mod_apto += 1

    elif ( profundidad >= 25 and profundidad <= 50 ):
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

    total_temp += temperatura
    total_prof += profundidad
    contador += 1
    n_entradas -= 1

######################################
print()
print("{0:.2f}".format(total_temp / contador))
print("{0:.2f}".format(total_prof / contador))
print(f"sumamente apto {sumamente_apto}")
print(f"moderadamente apto {moderadamente_apto}")
print(f"marginalmente apto {marginalmente_apto}")
print(f"no apto {nada_apto}")