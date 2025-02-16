#Valores de cada artículo en la tienda
precio_camiseta = 10.0
precio_sudadera = 20.5 
precio_gorra = 5.5
iva = 0.21

#Pedir al usuario que introduzca la cantidad de cada artículo
cantidad_camisetas = int(input("Introduzca la cantidad de camisetas que quiere comprar: "))
cantidad_sudaderas = int(input("Introduzca la cantidad de sudaderas que quiere comprar: "))
cantidad_gorras = int(input("Introduzca la cantidad de gorras que quiere comprar: "))

#Hacer las operaciones
valor_total_sin_iva = (cantidad_camisetas * precio_camiseta) + (cantidad_sudaderas * precio_sudadera) + (cantidad_gorras * precio_gorra)
valor_total_con_iva = valor_total_sin_iva + (valor_total_sin_iva * iva)

#Mostrar el total de la compra sumando el 21% de IVA.
print("\nResumen de la compra:")
print("El valor total de la compra es: ", valor_total_sin_iva, "euros")
print("El valor total de la compra con IVA 21% incluido es: ", valor_total_con_iva, "euros")
