print("Ministerio de Agricultura y Desarrollo Rural \n"
      "Programa para recuperar los suelos para el cultivo del cacao")

temperatura = float(input("Ingrese la temperatura (grados C): "))
profundidad = float(input("Ingrese la profundidad (cm): "))

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
    print("NO APTO")
elif (mar_apto > 0):
    print("MARGINALMENTE APTO")
elif (mod_apto > 0):
    print("MODERADAMENTE APTO")
else:
    print("SUMAMENTE APTO")