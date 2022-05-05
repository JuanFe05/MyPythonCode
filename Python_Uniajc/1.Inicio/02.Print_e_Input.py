nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))

######################################################################

print("Hola " + nombre + " " + apellido + " tienes una edad de: " + str(edad) + " años.")

print("Hola", nombre, " ", apellido, " tu edad es:", edad)

######################################################################

# Si la variable es un decimal, usaremos el operador %d
# Si es una cadena, usaremos el operador %s
print("Hola %s %s tienes un edad de %i años." % (nombre, apellido, edad))

######################################################################

# La letra f indica que la cadena se utiliza con el propósito de formatear.
print(f"Hola {nombre} {apellido} tu edad es de {edad} años")
print(f"Hola {nombre} {apellido} tu edad es de {edad ** 2} años") # Edad elevada al cuadrado

print(f"hola {nombre}")
print("Hola", nombre)

######################################################################

# Cuando usamos formato de cadena, podemos usar {} para marcar el lugar en la declaración donde la variable necesita ser sustituida.
print("Hola {} {} tu edad es: {} años".format(nombre, apellido, edad))

######################################################################