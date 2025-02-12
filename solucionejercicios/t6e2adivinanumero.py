# Función para comprobar si el usuario adivinó el número correcto
def comprobar_adivinanza(numero):
    numero_ganador = 4  # El número correcto es el 4
    mensaje = ""  # Variable para almacenar el mensaje
    
    # Asignar el mensaje dependiendo de si adivinó o no
    if numero == numero_ganador:
        mensaje = "¡Has ganado! El número es correcto."
    else:
        mensaje = f"Lo siento, perdiste. El número correcto era el {numero_ganador}."
    
    return mensaje  # Devolver el mensaje final

# Función principal
def juego_adivinanza():
    # Pedir al usuario que ingrese un número entre 1 y 10
    numero_usuario = int(input("Introduce un número del 1 al 10: "))

    # Obtener y mostrar el mensaje según la adivinanza
    mensaje = comprobar_adivinanza(numero_usuario)
    print(mensaje)

# Llamada a la función principal
juego_adivinanza()

