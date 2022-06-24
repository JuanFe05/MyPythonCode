num = int(input('Ingrese un numero del 1 al 10: '))

while num <= 0 or num > 10:
    num = int(input('Ingrese un numero del 1 al 10: '))

dicRoman = {1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X'}

print('El numero %d en romano es: ' %num,dicRoman.get(num))

########################################################################################################################
# numerosRomanos = { 1 : 'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII',8:'VIII',9:'IX',10:'X'}
#
# numero = int(input("Numero del 1 al 10: "))
#
# if numero >= 1 and numero <= 10:
#     print("El numero es ", numerosRomanos[numero])
# else:
#     print(" numero debe ser del  1 al 10")