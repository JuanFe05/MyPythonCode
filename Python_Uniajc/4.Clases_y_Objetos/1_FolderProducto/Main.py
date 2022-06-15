from Productos import Producto

p1 = Producto(1, "Producto 1", 1500)
p2 = Producto(2, "Producto 2", 2580)
p3 = Producto(3, "Producto 3", 1860)

#p1.nombre = "Producto Importado"

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(10))
print(p2.calcular_total(16))
print(p3.calcular_total(20))
