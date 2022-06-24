import random

def numAleatorio():
    while True:
        aleatorio = random.randint(100,131)

        if aleatorio not in (110,115,120):
            break

    return aleatorio

def numeros():
    for i in range(10):
        print(numAleatorio())

numeros()