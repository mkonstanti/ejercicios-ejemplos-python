#Lista de los 8 planetas
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Júpiter", "Saturno", "Urano", "Neptuno"]

#Definir funcion para elegir número y mostrar planeta
def juegoPlanetas():
    numero_elegido = int(input("Introduzca un numero de 1 a 8: "))
    if (1<= numero_elegido <=8) :
        planeta = planetas[numero_elegido - 1]
        print(f"El planeta que ha elegido es {planeta}")
    else:
        print("Debe introducir un número entre 1 y 8")
    
juegoPlanetas()
