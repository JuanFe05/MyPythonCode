semaforo = input("Ingrese la luz del semáforo: \n Verde - Amarillo - Rojo: ")
hayPeaton = input("SI o No: ")

if semaforo.lower() == "verde":
    if hayPeaton.lower() == "si":
        print("PARE")
    else:
        print("SIGA")

elif semaforo.lower() == "amarillo":
    if hayPeaton.lower() == "si":
        print("PARE")
    else:
        print("PRECAUCIÓN")

elif semaforo.lower() == "rojo":
    print("PARE")

else:
    print("INGRESE UNO DE LOS TRES COLORES O VALORES INDICADOS.")