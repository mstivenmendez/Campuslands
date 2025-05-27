utiles = []
cantidad = []
precio = []
entrada = True




while entrada :
    print ("ingrese su opcion")
    print ("1. agregar nuevos elementos  a la lista ")
    print ("2. lista de los elemnetos disponibles ")
    print ("3. actualizar lista ")
    print ("4 eliminar producto ")
    print ("0. salir  ")
    opcion = int(input("ingrese su opcion"))

    if opcion == 1 :
        while entrada :
            utiles.append(input("ingrese el utiles "))
            cantidad.append(int(input("ingrese la cantidad de los utiles")))
            precio.append(float(input("ingrese el valor del producto")))
            print ("1 para continuar y 2 para salir")
            salida = int(input("deseas ingresar mas productos"))
            if salida == 2 :
                break
    
    if opcion == 2 :
        for indice in range(len(utiles)) :
            print (f"el util es : {utiles[indice]} y su cantidad es: {cantidad[indice]} y su precio es: {precio[indice]}")
    
    if opcion == 3 :
        modificar = int(input("ingrese la posicion que quiere modificar"))
        for indice in range(len(utiles)) :
            if indice == modificar :
                actualizar = input("ingrese la modifiacion")
                utiles[indice] = actualizar
                actualizar_cantidad = int(input("ingrese la cantidad quye modificar"))
                cantidad[indice] = actualizar_cantidad
                actualizar_precio= float(input("ingrese la valor que va modificar"))
                precio[indice] = actualizar_precio

    if opcion == 4 :
        valor_eliminar = int(input("ingrese la posicion que quiere eliminar"))
        for indice in range(len(utiles)):
            if indice == valor_eliminar :
                utiles.pop[indice]
                cantidad.pop[indice]
                precio.pop[indice]

    if opcion == 0 :
        break

            

    