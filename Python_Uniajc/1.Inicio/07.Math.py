import math

pi = 3.1416
x = 1
y = 2
z = 3
i = -4.1111

#Redondea un número a n decimales.
print("round:", round(pi, 2)) 

#Redondea un número HACIA ARRIBA al entero más cercano.
print("ceil:", math.ceil(pi))  

# Redondea un número HACIA ABAJO al entero más cercano.
print("floor:", math.floor(pi))

#Valor absoluto
print("abs", abs(i)) 

#Potencia
print("potencia", pow(pi, 2))

print("raiz", math.sqrt(420))

print("raiz + round", round(math.sqrt(420), 4))

print("máximo de 3 numeros: ", max(x, y, z))

print("mínimo de 3 numeros: ", min(x, y, z))
