# Función para convertir euros a dólares
def convertir_a_dolares(euros):
    return euros * 1.1  # Tasa de conversión de 1 euro = 1.1 dólares

# Función para convertir euros a libras
def convertir_a_libras(euros):
    return euros * 0.87  # Tasa de conversión de 1 euro = 0.87 libras

# Función principal para gestionar la conversión
def conversor_de_monedas():
    euros = float(input("Introduce la cantidad en euros: "))  # Solicitar la cantidad en euros

    dolares = convertir_a_dolares(euros)  # Llamar a la función para convertir a dólares
    libras = convertir_a_libras(euros)    # Llamar a la función para convertir a libras

    # Mostrar los resultados de forma clara
    print("Cantidad en euros:", euros)
    print("Equivalente en dólares:", dolares)
    print("Equivalente en libras:", libras)

# Llamar a la función principal
conversor_de_monedas()
