from Empleados import Empleado

nombre = input("Ingresa el nombre del empleado: ")
apellido = input("Ingresa el apellido del empleado: ")

ep1 = Empleado(nombre, apellido)

for i in range(5):
    salarios = int(input(f"Ingresa el salario número {i + 1}: "))
    
    while salarios <= 0:
        salarios = int(input(f"Ingresa el salario número {i + 1}: "))
    
    ep1.addSalarios(salarios)

print(ep1.nombre, ep1.apellido)
print(*ep1.salarios)  # El * me permite imprimir la lista de forma normal