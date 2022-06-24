semaforo = input("Ingrese la luz del semáforo: \n Verde - Amarillo - Rojo: ")

if semaforo.lower() == "verde":
    print("SIGA")

elif semaforo.lower() == "amarillo":
    print("PRECAUCIÓN")

elif semaforo.lower() == "rojo":
    print("PARE")

else:
    print("INGRESE UNO DE LOS TRES COLORES O VALORES INDICADOS.")