def recortar(numero, minimo, maximo):
    if numero < minimo:
        return minimo
    elif numero > maximo:
        return maximo
    return numero

num = 15
min = 0
max = 10
print( recortar(num, min, max))