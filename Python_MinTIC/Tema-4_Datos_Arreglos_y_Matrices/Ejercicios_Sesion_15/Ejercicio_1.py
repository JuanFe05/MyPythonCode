def actividad1():
    frase = input("Ingresa una frase: ").split()
    numero = int(input("Ingresa un número: "))
    
    palabras = []
    
    for i in frase:
        palabras.append([i])
        
        if len(i) > numero:
            print(i)

actividad1()