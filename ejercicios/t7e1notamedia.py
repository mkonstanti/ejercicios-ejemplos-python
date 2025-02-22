# Definir la función para calcular la media nota
def calcular_media_nota(): 
    #Pedir al usuario la cantidad de notas
    cantidad_notas = int(input("Cuantas notas quieres introducir? "))
    #Inicializar suma_notas antes del bucle
    suma_notas = 0
    for i in range(cantidad_notas):
        nota = float(input(f"Introduce la nota {i+1}: "))
        suma_notas += nota
    media_nota = suma_notas / cantidad_notas
    #Mostrar la media nota en la consola
    print(f"La media de las {cantidad_notas} notas es {media_nota:.2f}")

#Llamamos la función
calcular_media_nota()




