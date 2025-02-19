# Función para mostrar el mensaje según el número elegido
def mensaje_destino(numero):
    numero_ganador = 4  # El número correcto es el 4
    mensaje = ""  # Variable para almacenar el mensaje

    # Usamos condicionales para asignar el mensaje correcto
    if numero == numero_ganador:
        mensaje = "¡Has ganado! El número es correcto."
    elif (10 >= numero > 4):
        mensaje = f"Lo siento, perdiste. El número correcto era el {numero_ganador}."
    elif (1 <= numero < 4):
        mensaje = f"Lo siento, perdiste. El número correcto era el {numero_ganador}."
    else:
        mensaje = "Número no reconocido. Por favor elige un número entre 1 y 10"
    
    return mensaje  # Devolver el mensaje final

# Función principal
def adivinar_el_numero():
    # Pedir al usuario que elija un número
    número = int(input("Elige un número de 1 a 10 y adivina el número correcto: "))

    # Mostrar el mensaje relacionado con el color
    mensaje = mensaje_destino(número)
    print(mensaje)

# Llamada a la función principal
adivinar_el_numero()
