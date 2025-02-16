#Pedir al usuario que introduzca una frase
frase = input("Introduce una frase: ")

#Obtener la longitud y la frase en mayúsculas y minúsculas
longitud = len(frase)
frase_mayusculas = frase.upper()
frase_minusculas = frase.lower()

#Mostrar la longitud de la frase
print("La longitud de la frase es", longitud)

#Mostrar la frase en mayúsculas.
print("La frase en mayúsculas:", frase_mayusculas)

#Mostrar la frase en minúsculas.
print("La frase en minúsculas:", frase_minusculas)