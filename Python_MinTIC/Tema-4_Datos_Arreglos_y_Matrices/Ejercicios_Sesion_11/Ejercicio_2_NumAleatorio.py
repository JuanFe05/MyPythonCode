import random

def mayor(x):
    numMayor = max(x)
    print(f"El número mayor es: {numMayor}")

def primos(x):
    primos = []
    for i in x:
        p = 0
        if i != 1:
            for j in range(1, i + 1):
                if i % j == 0:
                    p += 1
            if p == 2:
                primos.append(i)

    print(f"Los número primos son: {primos}")

def principal():
    listNumeros = []
    contador = 0

    while contador < 6:
        numAleatorio = random.randint(1,20)

        listNumeros.append(numAleatorio)
        contador = contador + 1

    print(f"Número aleatorios: {listNumeros}")
    mayor(listNumeros)
    primos(listNumeros)

principal()