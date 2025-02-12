#Guardamos la ciudad del usuario
ciudad = input("Introduce tu ciudad: ")
#unimos 2 cadenas
bienvenida = "Bienvenidos a " + ciudad
#obtenemos el numero de letras de la cadena
longitud = len(bienvenida)
#poner la cadena en mayusculas
bienvenidamayusculas = bienvenida.upper()
#poner la cadena en minusculas
bienvenidaminusculas = bienvenida.lower()
#IMPRIMIR CADENAS
#imprimimos la palabra
print(bienvenida)
#imprimir la longitud (al ser un numero no puede ir solo)
print("Longitud ", longitud)
#imprimir cadena en mayusculas
print(bienvenidamayusculas)
#imprimir la cadena en minusculas
print(bienvenidaminusculas)