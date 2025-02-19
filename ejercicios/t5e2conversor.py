#Valores de tasas para dolar y libra
tasa_dolar = 1.1
tasa_libra = 0.87

#Definir función para conversión en dólares
def convertirEnDolares(cantidad_euros):
    cantidad_dolares = cantidad_euros * tasa_dolar
    return cantidad_dolares 

#Definir función para conversión en libras
def convertirEnLibras(cantidad_libras):
    cantidad_libras = cantidad_libras * tasa_libra
    return cantidad_libras

# Función principal para gestionar la conversión
def conversor_de_monedas():
    cantidad_euros = float(input("Introduce una cantidad en euros: "))

    cantidad_dolares = convertirEnDolares(cantidad_euros)
    cantidad_libras = convertirEnLibras(cantidad_euros)

    #Mostrar equivalente en dólares y libras
    print(f"\nLa cantidad en euros es {cantidad_euros} ")
    print(f"La cantidad en dólares es {cantidad_dolares} ")
    print(f"La cantidad en libras es {cantidad_libras} ")

# Llamar a la función principal
conversor_de_monedas()

