#Pedir al usuario que introduzca una dirección de correo electrónico
correo = input("Introduce una dirección de correo electrónico: ")

#Obtener la longitud y el correo en mayúsculas y minúsculas
longitud_correo = len(correo)
correo_mayusculas = correo.upper()
correo_minusculas = correo.lower()

#Mostrar la longitud del correo
print("La longitud de la dirección de correo es", longitud_correo)

#Mostrar el correo en mayúsculas.
print("El correo en mayúsculas:", correo_mayusculas)

#Mostrar el correo en minúsculas.
print("El correo en minúsculas:", correo_minusculas)

