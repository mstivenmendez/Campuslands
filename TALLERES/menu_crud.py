
despensa  = []
ingresos = []
def menu_crud():
    while True:
        print("\nMenu CRUD")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Listar productos")
        print("5. Salir")

        def agregar_producto():
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            despensa.append({'nombre': nombre, 'cantidad': cantidad, 'precio': precio})
            print(f"Producto '{nombre}' agregado exitosamente.")
        def actualizar_producto():
            nombre = input("Ingrese el nombre del producto a actualizar: ")
            for producto in despensa:
                if producto['nombre'] == nombre:
                    cantidad = int(input("Ingrese la nueva cantidad del producto: "))
                    precio = float(input("Ingrese el nuevo precio del producto: "))
                    producto['cantidad'] = cantidad
                    producto['precio'] = precio
                    print(f"Producto '{nombre}' actualizado exitosamente.")
                    return
            print(f"Producto '{nombre}' no encontrado.")
        def eliminar_producto():
            nombre = input("Ingrese el nombre del producto a eliminar: ")
            for producto in despensa:
                if producto['nombre'] == nombre:
                    despensa.remove(producto)
                    print(f"Producto '{nombre}' eliminado exitosamente.")
                    return
            print(f"Producto '{nombre}' no encontrado.")
        def listar_productos():
            if not despensa:
                print("No hay productos en la despensa.")
            else:
                print("Productos en la despensa:")
                for producto in despensa:
                    print(f"Nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
        

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            actualizar_producto()
        elif opcion == '3':
            eliminar_producto()
        elif opcion == '4':
            listar_productos()
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intente de nuevo.")
    
# Llamada a la función para iniciar el menú CRUD
# Este código implementa un menú CRUD para gestionar productos en una despensa.
# Permite agregar, actualizar, eliminar y listar productos.
# El menú se ejecuta en un bucle hasta que el usuario decide salir.