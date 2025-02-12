# Función para mostrar el mensaje según el color elegido
def mensaje_destino(color):
    mensaje = ""  # Variable para almacenar el mensaje

    # Usamos condicionales para asignar el mensaje correcto
    if color == "ROJO":
        mensaje = "El rojo es el color de la pasión y la energía. ¡Hoy será un día lleno de acción y emoción! No temas a los desafíos, saldrás victorioso."
    elif color == "VERDE":
        mensaje = "El verde representa la esperanza y el crecimiento. Algo nuevo y positivo está por florecer en tu vida. Confía en los pequeños cambios que te acercan a tus metas."
    elif color == "AZUL":
        mensaje = "El azul simboliza la calma y la serenidad. Hoy estarás rodeado de tranquilidad y equilibrio. Aprovecha este momento para reflexionar y renovar tu energía."
    elif color == "AMARILLO":
        mensaje = "El amarillo es el color de la felicidad y el optimismo. ¡Prepárate para un día lleno de alegría y buenas noticias! Alguien cercano te sorprenderá de forma positiva."
    elif color == "MORADO":
        mensaje = "El morado evoca la sabiduría y la creatividad. Hoy te sentirás inspirado y lleno de ideas. Es el momento ideal para dejar volar tu imaginación y tomar decisiones importantes."
    else:
        mensaje = "Color no reconocido. Por favor elige uno de los siguientes colores: Rojo, Verde, Azul, Amarillo o Morado."
    
    return mensaje  # Devolvemos el mensaje final

# Función principal
def ruleta_de_colores():
    # Pedir al usuario que elija un color
    color = input("Elige tu color favorito (Rojo, Verde, Azul, Amarillo, Morado): ")

    # Convertimos la entrada a mayúsculas para no depender del caso
    color = color.upper()

    # Mostrar el mensaje relacionado con el color
    mensaje = mensaje_destino(color)
    print(mensaje)

# Llamada a la función principal
ruleta_de_colores()
