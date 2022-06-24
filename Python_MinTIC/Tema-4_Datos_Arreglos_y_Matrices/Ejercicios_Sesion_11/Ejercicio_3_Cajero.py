def caja():
    continuar = ""
    nombres = []
    productos = []
    precio_total = n_productos = 0

    while continuar != "n":
        nombre = input("\nIngresa nombre del producto: ")
        producto = int(input("Ingresa le precio del producto: "))

        nombres.append(nombre)
        productos.append(producto)

        continuar = input("Desea Ingresar otro producto (S/Si, N/No): ").lower()

        while continuar != "s" and continuar != "n":
            continuar = input("Desea Ingresar otro producto (S/Si, N/No): ").lower()

        precio_total = sum(productos)
        n_productos += 1

    imprimaProducto(nombres, productos, precio_total, n_productos)

########################## Funcion imprimaProductos #########################
def imprimaProducto(nombres, productos, precio_total, n_productos):

    for i in range(n_productos):
        print(f"-> Producto N° {i + 1} Nombre: {nombres[i]} Precio : {productos[i]}")

    print("\nPrecio Total: ",precio_total)

caja()