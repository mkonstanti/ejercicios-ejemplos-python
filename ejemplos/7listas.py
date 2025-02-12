#Lista de notas. Numeros
notas = [4, 6, 8, 10]
#Lista de nombres. Textos
nombres = ["Juan", "Maria", "Antonio", "Ana" ]

#Agregar un nuevo nombre a la lista
nombre = input("Introduce un nombre: ")
nombres.append(nombre)

notas.append(11)

#Imprimir la lista
print(notas)
print(nombres)

#Eliminar un elemento de la lista
notaAeliminar = float (input("introduce la nota que desea eliminar: "))
notas.remove(notaAeliminar)
nombreAeliminar = input("Introduzca el nombre que desea eliminar")
nombres.remove(nombreAeliminar)

#Imprimir la lista
print(notas)
print(nombres)

#Mostrar el segundo alumno de la lista
print("Alumno en la posicion 2", nombres[1])