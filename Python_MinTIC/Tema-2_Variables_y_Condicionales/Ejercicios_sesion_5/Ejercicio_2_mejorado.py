semaforo = input("Ingrese la luz del semáforo: \n Verde - Amarillo - Rojo: ")
hayPeaton = input("SI o No: ")

if semaforo.lower() == "verde" or semaforo.lower() == "amarillo":
    if hayPeaton.lower() == "si":
        print("PARE")
    elif hayPeaton.lower() == "no" and semaforo.lower() == "verde":
        print("SIGA")
    else:
        print("PRECAUCION")

elif semaforo.lower() == "rojo":
    print("PARE")

else:
    print("INGRESE UNO DE LOS TRES COLORES O VALORES INDICADOS.")