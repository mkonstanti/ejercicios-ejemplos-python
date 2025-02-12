def calcular_nota_media ():
    #Guardamos la cantidad de notas que va a introducir el usuario
    num_notas = int(input("Cuantas notas quieres introducir?"))
    #Repetimos pedir al usuario el numero de veces que ha indicado. Si ha indicado 3 notas se repetira 3 veces.
    for i in range(num_notas):
        #En cada repeticion guardamos la nota
        nota = float(input("Introduce la nota"))
        #La sumamos al total
        suma += nota
    #Calculamos la media, que es igual a la suma total, entre el numero de notas introducida
    nota_media = suma/num_notas

    print("Nota media es: ", nota_media)


calcular_nota_media()