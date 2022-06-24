base = int(input('Ingresa el número de filas: '))

#pirámide normal
espacios = base-1
simbolos = 1
for lines in range(base):
    while espacios >= 0:
        print ('%s%s%s' % ((' ' * espacios), ('*' * simbolos), (' ' * espacios)))
        espacios -= 1
        simbolos += 2

#pirámide invertida
espacios = 0
simbolos = (base * 2) - 1
for lines in range(base):
    while espacios <= (base-1):
        print ('%s%s%s' % ((' ' * espacios), ('*' * simbolos), (' ' * espacios)))
        espacios += 1
        simbolos -= 2