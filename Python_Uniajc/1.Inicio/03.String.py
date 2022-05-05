#Vamos a comprobar si un string es un string vacío
""" cadena = " "

print("==", cadena == "")
print("is", cadena is "")
print("not", not cadena)  """ #forma recomendada

##############################################################

""" palabra = "Hola"
repetir = palabra * 4
print(repetir) """

##############################################################

nombre = "Camilo"

# longitud del nombre (# de letras)
print(len(nombre))

#El método capitalize() convierte el primer carácter de una cadena en mayúsculas y todos los demás caracteres en minúsculas, si los hay.
print(nombre.capitalize()) 

#El método upper() convierte todos los caracteres en minúsculas de una cadena en caracteres en mayúsculas y los devuelve.
print(nombre.upper())

#El método lower() convierte todos los caracteres en mayúsculas de una cadena en caracteres en minúsculas y los devuelve.
print(nombre.lower())

#El método isdigit() devuelve True si todos los caracteres de una cadena son dígitos. Si no, devuelve False.
print(nombre.isdigit())

#El método isalpha() devuelve True si todos los caracteres de la cadena son alfabetos. Si no, devuelve False.
print(nombre.isalpha())

#El método count() devuelve el número de ocurrencias de una subcadena en la cadena dada.
print(nombre.count("i"))

#El método replace() reemplaza cada coincidencia del carácter/texto antiguo en la cadena con el nuevo carácter/texto.
print(nombre.replace("o", "a"))