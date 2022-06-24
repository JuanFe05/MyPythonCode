def insercion():
    print()
    print("----Inserción en lista ordenada----")
    V = [2, 5, 15, 20, 35, 50]
    print("Lista original: ", V)
    pos = 0
    numero = int(input(" Número a insertar: "))  # 16

    while (pos <= len(V)-1 and V[pos] < numero):
        pos += 1
    #print("Posicion", pos)
    V.append(0)
    for i in range(len(V)-1, pos-1, -1):
        V[i] = V[i-1]

    V[pos] = numero
    print("Nueva lista ordenada es: ", V)

def insercion_desordenado_fijo():
    print()
    print("----Inserción en lista desordenada fija----")
    arreglo = [89, 23, 0, 15, 90]
    print(arreglo)
    posicion = int(input("Posición a insertar: "))
    if posicion-1 <= len(arreglo)-1:
        numero = int(input("Número a insertar: "))
        i=0
        while(i<=len(arreglo)-1):
            if i == posicion-1:
                arreglo[i] = numero
                break
            i += 1
        print(arreglo)
    else:
        print("Posición fuera de rango")

def insercion_desordenado_variable():
    print()
    print("----Inserción en lista desordenada variable----")
    arreglo = [89, 23, 0, 15, 90, 0]
    print(arreglo)
    posicion = int(input("Posición a insertar: "))
    if(posicion-1 <= len(arreglo)-1):
        numero = int(input("Número a insertar: "))
        i=0
        while(i<=len(arreglo)-1):
            if i == posicion-1:
                arreglo.append(0)
                break
            i += 1
        pos = i
        aux = arreglo[pos]
        for i in range(len(arreglo)-1, pos-1, -1):
            arreglo[i] = arreglo[i-1]
        # print(V[i])
        arreglo[pos] = numero
        print(arreglo)
    else:
        print("Fuera de rango, no se puede insertar el número")

def menu():
    op = 0
    while(op != 4):

        print("1. Inserción en vector ordenado")
        print("2. Inserción en vector desordenado fijo")
        print("3. Inserción en vector desordenado variable")
        print("4. Salir")

        op = int(input("Elija una opción: "))
        if op == 1:
            insercion()
        elif op == 2:
            insercion_desordenado_fijo()
        elif op == 3:
            insercion_desordenado_variable()
        elif (op == 4):
            print("Todo tiene su final.")
        else:
            print("Elija una opción válida.")

menu()