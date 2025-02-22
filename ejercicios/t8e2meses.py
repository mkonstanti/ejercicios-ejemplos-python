#Lista de los meses del año
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
#Definir funcion para mostrar el mes correspondiente y si es el mejor mes
def mostrar_mes():
    numero_elegido = int(input("Introduce un número del 1 al 12 para conocer el mes: "))
    if 1 <= numero_elegido <= 12: 
        indice = numero_elegido - 1
        mes = meses[indice]
        if indice == 5 : 
            print(f"El mes correspondiente al número {numero_elegido} es {mes} y es EL MEJOR MES")
        else: 
            print(f"El mes correspondiente al número {numero_elegido} es {mes}")

    else:
        print("El número es inválido, debe introducir un número entre 1 y 12")

mostrar_mes()