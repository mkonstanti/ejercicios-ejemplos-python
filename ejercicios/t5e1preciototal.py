# Definir función para calcular el descuento
def calcular_descuento(subtotal, descuento):
    return subtotal * (descuento / 100)

# Definir función para calcular el IVA
def calcular_iva(subtotal, iva):
    return subtotal * (iva / 100)

def calcular_precio_final(precio, cantidad, descuento, iva):
    total_precio = precio * cantidad
    descuento_aplicado = calcular_descuento(total_precio, descuento)
    precio_con_descuento = total_precio - descuento_aplicado
    iva_aplicado = calcular_iva(precio_con_descuento, iva)
    precio_total = precio_con_descuento + iva_aplicado
    return precio_total

#Pedir al usuario que introduzca los datos
nombre_producto = input("Introduce el nombre del producto: ")
precio_producto = float(input("Introduzca el precio del producto: "))
cantidad = int(input("Introduzca la cantidad de productos que desea comprar: "))
descuento = float(input("Introduzca en porcentaje el descuento: "))
iva = float(input("Introduzca en porcentaje en IVA: "))

#Calcular el precio final
precio_final = calcular_precio_final(precio_producto, cantidad, descuento, iva)

#Mostrar el precio final 
print("\nResumen de la compra:")
print(f"\nEl precio total del producto '{nombre_producto}' es: {precio_final} euros")