import math

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))
c = int(input("Ingrese el valor de c: "))
d = int(input("Ingrese el valor de d: "))
x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
z = int(input("Ingrese el valor de z: "))

expresion_1 = math.sqrt(pow(b, 2)) - (4 * a * c) # pow(x, y) exponencia de valores
expresion_2 = ((pow(x, 2)) + (pow(y, 2))) / (pow(z, 2))
expresion_3 = ((3 * x) + (2 * y)) / (2 * z) 
expresion_4 = (a + b) / (c - d)
expresion_5 = (4 * pow(x, 2)) - (2 * x) + 7
expresion_6 = ((x + y) / x) - ((3 * x) / 5)

print(f"Resultado expresión 1: {expresion_1}")
print("Resultado expresión 2: " + str(expresion_2))
print("Resultado expresión 3: " + str(expresion_3))
print("Resultado expresión 4: " + str(expresion_4))
print("Resultado expresión 5: " + str(expresion_5))
print("Resultado expresión 6: " + str(expresion_6))