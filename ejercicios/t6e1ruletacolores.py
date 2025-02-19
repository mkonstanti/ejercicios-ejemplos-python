def mensaje_color(color):
    if (color == "ROJO"):
        mensaje = "El rojo es el color de la pasión y la energía. ¡Hoy será un día lleno de acción y emoción! No temas a los desafíos, saldrás victorioso."
    elif (color == "VERDE"):
        mensaje = "El verde representa la esperanza y el crecimiento. Algo nuevo y positivo está por florecer en tu vida. Confía en los pequeños cambios que te acercan a tus metas."
    elif (color == "AZUL"):
        mensaje = "El azul simboliza la calma y la serenidad. Hoy estarás rodeado de tranquilidad y equilibrio. Aprovecha este momento para reflexionar y renovar tu energía."
    elif (color == "AMARILLO"):
        mensaje = "El amarillo es el color de la felicidad y el optimismo. ¡Prepárate para un día lleno de alegría y buenas noticias! Alguien cercano te sorprenderá de forma positiva."
    elif (color == "MORADO"):
        mensaje = "El morado evoca la sabiduría y la creatividad. Hoy te sentirás inspirado y lleno de ideas. Es el momento ideal para dejar volar tu imaginación y tomar decisiones importantes."
    else: 
        mensaje = "Ese color no está en la ruleta. Intenta con Rojo, Verde, Azul, Amarillo o Morado."
    return mensaje

#Pedimos al usuario que introduzca un color
def ruleta_colores():
    color_elegido = input("Introduce un color: ")

    color_mayusculas = color_elegido.upper()

#Llamar a la ruleta de colores para que nos muestre el mensaje 
    mensaje = mensaje_color(color_mayusculas)

#Mostrar el mensaje al usuario
    print("\nTu color elegido es " + color_mayusculas)
    print(mensaje)

# Llamar a la función principal
ruleta_colores()
