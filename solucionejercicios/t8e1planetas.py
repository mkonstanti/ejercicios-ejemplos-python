# Lista de planetas del sistema solar
planetas = ["Mercurio", "Venus", "Tierra", "Marte", "Jupiter", "Saturno", "Urano", "Neptuno"]

def mostrar_planeta(numero):
    if 1 <= numero <= 8:
        planeta = planetas[numero - 1]
        mensaje = "El planeta correspondiente es: " + planeta
    else:
        mensaje = "Número inválido, introduce un número entre 1 y 8."
    return mensaje

# Solicitar al usuario que ingrese un número del 1 al 8
numero = int(input("Introduce un número del 1 al 8 para conocer el planeta: "))

# Llamar a la función y mostrar el resultado
resultado = mostrar_planeta(numero)
print(resultado)
