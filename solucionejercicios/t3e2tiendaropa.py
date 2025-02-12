# Precios de los productos
precio_camiseta = 10.0
precio_sudadera = 20.5
precio_gorra = 5.5
iva = 0.21  # IVA del 21%

# Pedir al usuario que introduzca las cantidades de cada producto
cantidad_camisetas = int(input("Introduce la cantidad de camisetas: "))
cantidad_sudaderas = int(input("Introduce la cantidad de sudaderas: "))
cantidad_gorras = int(input("Introduce la cantidad de gorras: "))

# Calcular el subtotal de la compra
subtotal = (cantidad_camisetas * precio_camiseta +
            cantidad_sudaderas * precio_sudadera +
            cantidad_gorras * precio_gorra)

# Calcular el IVA y el total con IVA
iva_total = subtotal * iva
total_compra = subtotal + iva_total

# Mostrar el total de la compra
print("\nResumen de la compra:")
print("Subtotal:", subtotal, "euros")
print("IVA (21%):", iva_total, "euros")
print("Total con IVA:", total_compra, "euros")
