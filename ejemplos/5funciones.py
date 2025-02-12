#Definimos una funcion sin parametros
def saludar():
    print("Hola que tal ")

#Definir funciones que reciben y devuelven parametros
def saludarConNombre(nombre):
    saludo = "Hola que tal " + nombre
    return saludo

#Llamamos a la funcion
saludar()
saludar()

#En primer lugar guardamos el nombre
nombre = input("Introduce tu nombre: ")
saludo = saludarConNombre(nombre)
print(saludo)

nombre2 = input("Introduce tu nombre 2: ")
saludo2 = saludarConNombre(nombre2)
print(saludo2)