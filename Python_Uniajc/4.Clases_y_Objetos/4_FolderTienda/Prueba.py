from Tienda import Tienda
from Computador import Computador

tienda1 = Tienda("Tienda Virtual", "Juan", 123456)

tienda1.agregarComputador(Computador("Asus", 1000, "AMD Ryzen™ 9 6980HX", "Windows 11", 12000000))
tienda1.agregarComputador(Computador("Acer", 500, "Intel Core™ i7-12800H", "Windows 11", 14600000))
tienda1.agregarComputador(Computador("Apple", 250, "M1 Max", "macOS", 16000000))

print("Lista de computadores")
tienda1.imprimirComputadores()
print()

print("Busca el computador por la marca")
tienda1.buscar("Asus")
print()

print("Elimina un computador y vuelve a imprimir la lista de computadores")
tienda1.eliminar("Apple")
tienda1.imprimirComputadores()
