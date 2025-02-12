# Función para aplicar el descuento
def aplicar_descuento(subtotal, descuento):
    descuento_aplicado = subtotal * (descuento / 100)
    return subtotal - descuento_aplicado

# Función para aplicar el IVA
def aplicar_iva(subtotal, iva):
    iva_aplicado = subtotal * (iva / 100)
    return subtotal + iva_aplicado

# Función principal que calcula el precio total
def calcular_precio_total(precio_unitario, cantidad, descuento, iva):
    # Calcular el subtotal (sin descuento ni IVA)
    subtotal = precio_unitario * cantidad

    # Aplicar el descuento
    subtotal_con_descuento = aplicar_descuento(subtotal, descuento)

    # Aplicar el IVA
    precio_final = aplicar_iva(subtotal_con_descuento, iva)

    return precio_final

# Pedir al usuario los datos
nombre_producto = input("Introduce el nombre del producto: ")
precio_unitario = float(input("Introduce el precio por unidad del producto: "))
cantidad = int(input("Introduce la cantidad de productos que deseas comprar: "))
descuento = float(input("Introduce el descuento en porcentaje: "))
iva = float(input("Introduce el IVA en porcentaje: "))

# Calcular el precio total llamando a la función
precio_total = calcular_precio_total(precio_unitario, cantidad, descuento, iva)

# Mostrar el resultado
print(f"\nEl precio total del producto '{nombre_producto}' es: {precio_total} euros")


