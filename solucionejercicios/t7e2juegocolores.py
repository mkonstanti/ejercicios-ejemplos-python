def juego_colores():
    #Pedimos al usuario 5 veces los colores.
    for i in range(5):
        color = input("Introduce un color")
        #Si el color es azul (lo pasamos a mayuscula para que de igual si ha puesto AZUL o azul). Ponemos la variable premio a true (para no mostrar hasta que termine de introducir los colores si ha ganado o no)
        if (color.upper() == "AZUL"):
            premio = True
    
    #Cuando termina de introducir los colores, si ha ganado el premio, se muestra el texto, sino se muestra que no ha ganado.
    if(premio):
        print("HA GANADO EL PREMIO")
    else:
        print("NO HA GANADO")

