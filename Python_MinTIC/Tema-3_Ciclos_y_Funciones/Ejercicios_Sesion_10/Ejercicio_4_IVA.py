def totalFactura(tFactura, iva = 0):

    if iva == 0:
        iva = 21
        total = tFactura + (iva / 100*tFactura)

    else:
        total = tFactura + (iva / 100 * tFactura)

    return total


tFactura = int(input("Ingrese el total de la factura: "))
iva = int(input("Ingrese le IVA a aplicar: "))

total = totalFactura(tFactura, iva)
print(f"El total de la factura es: {total}")