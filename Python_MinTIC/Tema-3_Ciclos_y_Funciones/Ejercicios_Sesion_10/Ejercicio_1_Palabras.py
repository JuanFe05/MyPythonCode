entrar = True
while entrar:
    cantidad_letras = 0
    tamaño_palabra = 0

    palabra = input("Ingresa una palabra: ").lower()
    letra = input("Ingresa una letra: ").lower()

    tamaño_palabra = len(palabra)

    for i in range(tamaño_palabra):
        if palabra[i] == letra:
            cantidad_letras += 1

    if cantidad_letras > 0:
        print(f"la letra {letra} se encuentra {cantidad_letras} veces en la palabra {palabra}")
        entrar = False

    else:
        print(f"la letra {letra} No se encuentra en la palabra {palabra}")