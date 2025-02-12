def mostrar_mes():
    # Lista de los meses del año
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    # Solicitar al usuario que ingrese un número del 1 al 12
    numero = int(input("Introduce un número del 1 al 12 para conocer el mes: "))
    # Si el mes es valido (entre 1 y 12)
    if 1 <= numero <= 12:
        #Obtenemos el mes de la lista, empieza en 0 asi que restamos 1
        mes = meses[numero - 1]
        #Si el mes es junio, indicamos en el mensaje el mejor mes, sino mostramos el mes.
        if mes == "Junio":
            mensaje = mes + " EL MEJOR MES"
        else:
            mensaje = "El mes correspondiente es: " + mes
    else:
        mensaje = "Número inválido, introduce un número entre 1 y 12."
    
    print(mensaje)


mostrar_mes()
