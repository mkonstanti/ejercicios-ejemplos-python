#Definir funcion para ver si el usuario ha ganado el premio
def juego_colores():
    print("Introduce 5 colores para ver si has ganado el premio")
    for i in range(5): 
        color = input(f"Introduce el color {i+1}: ")
        color_mayuscula = color.upper()
        if color_mayuscula == "AZUL":
            premio = True

    if (premio): 
        print("Has ganado el premio! El color ganador fue el azul")
    else: 
        print("No has ganado el premio")

juego_colores()



