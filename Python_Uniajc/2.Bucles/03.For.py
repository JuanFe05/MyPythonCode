import os, random, itertools

########################################################

# El for en python es muy parecido al foreach de java, este me permite recorrer cada elemento de un conjunto de datos, Por ejemplo:
numeros = [0, 1, 2, 3, 4, 5]
for numero in numeros:  
    print(numero)       

########################################################

""" num = int(input("Número del cual desea la tabla: "))

for i in range(1, 11):
    print(f"{num} * {i}:", i * num) """
    
########################################################
""" numNotas = int(input("Numero de notas que desea ingresar: "))

notas = 0

for i in range(0, numNotas):
    nota = float(input(f"nota {i+1}: "))
    notas += nota
    
print("Promedio de notas: ", (notas / numNotas)) """

########################################################
""" for i in range(1, 11):
    print('PROCESO ' + str(i))
    
    numero_al_azar = random.randint(0, 1000-1)
    
    print('Valor de numero al azar: ' + str(numero_al_azar)) """
    
########################################################
""" num = 10

for i in range(num):
    print(i + 1) """
    
########################################################
""" num = 10
for _ in itertools.repeat(None, num):
    print("Hola a todos") """

########################################################
""" diccionario = {1: "Colombia", 2: "Argentina"} #Esto es muy parecido a una matriz, se puede llamar, matriz asociativa

for clave, valor in diccionario.items():
    print(f"clave {clave} es el País {valor}") """
    
########################################################
lect = int(input("Ingrese cuantos número desea leer: "))

positivos = negativos = neutro = 0

for i in range(lect):
    num = float(input("Número: "))

    if num == 0:
        neutro += 1

    elif num < 0:
        negativos += 1

    else:
        positivos += 1

print(f"Hay {positivos} Positivos, {negativos} Negativos y {neutro} Neutros")
