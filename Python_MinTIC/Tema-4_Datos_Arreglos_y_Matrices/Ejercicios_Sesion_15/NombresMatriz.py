nombres = ['Ana', 'Sonia', 'Helena']
nombres2 = ['Miguel', 'Carlos', 'Juan']
nombresFinales = [nombres, nombres2]

for i in range(len(nombresFinales)):
    print ('\n')
    if i == 0:
        print ('###### NOMBRES FEMENINOS #####')
    elif i == 1:
        print ('###### NOMBRES MASCULINOS #####')

    for j in range(len(nombresFinales[i])):
        print (nombresFinales [i][j], end=', ')