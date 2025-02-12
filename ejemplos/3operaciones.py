#Pedir al usuario que introduzca 2 numeros
#Convertimos a numero. int (sin decimales), float(puede tener decimales)
numero1 = float(input("Introduzca un numero: "))
numero2 = float(input("Introduzca otro numero: "))

#Hacemos las operaciones

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

media = (numero1 + numero2) / 2

#Imprimimos los resultados
print("Suma ", suma)
print("Resta ", resta)
print("Multiplicacion ", multiplicacion)
print("Division ", division)
print("Media ", media)