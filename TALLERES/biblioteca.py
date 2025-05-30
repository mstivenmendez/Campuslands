
# BLIOTECA DE LIBLOS ctl+k+s
import os

def clear_screen():
    # Función para limpiar la pantalla
    if os.system.name == 'nt' :
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Linux/Unix


def menu_principal():
    # Función para mostrar el menú principal
    print("EL MENÚ DE LA BIBLIOTECA")
    print("1. GESTIONAR LIBROS")
    print("2. PRESTAMOS DE LIBROS")
    print("3. DEVOLUCIONES DE LIBROS")
    print("4. LISTAR LIBROS PRESTADOS") 
    print("5. LISTAR LIBROS ")
    print("6. HISTORIAL DE PRESTAMOS")
    print("0. SALIR")
    print("=====================================")

def sub_menu():
    # Función para mostrar el submenú de gestión de libros
    print("GESTION DE LIBROS")
    print("1. AGREGAR LIBROS")
    print("2. ACTUALIZAR LIBROS")
    print("3. ELIMINAR LIBROS")
    print("4. LISTAR LIBROS")
    print("0. VOLVER AL MENÚ PRINCIPAL")
    print("=====================================")


def validacion_ingreso(mensaje: str, valorminimo: int = 0, valormaximo: int = 6):
    # Función para validar el ingreso de datos
    while True:
        try:
            valor = int(input(mensaje))
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.")
                menu_principal()
        except:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def ingresar_libro():
    # Función para ingresar un libro
    codigo = int(input("Ingrese el código del libro: "))
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    editorial = input("Ingrese la editorial del libro: ")

    while True:
        menu_principal()
        opcion = validacion_ingreso("ELIGE UNA OPCION: ", 0, 6)

        if opcion == 1 :
            while True:
                sub_menu()
                sub_opcion1 = validacion_ingreso("ELIGE UNA OPCION: ", 0, 4)
            
            if sub_opcion1 == 1:
                print("AÑADIENDO LIBRO...")
                # Aquí iría el código para añadir un libro
            elif sub_opcion1 == 2:
                print("ACTUALIZANDO LIBRO...")
                # Aquí iría el código para actualizar un libro
            elif sub_opcion1 == 3 :
                print("ELIMINANDO LIBRO...")
                # Aquí iría el código para eliminar un libro
            elif sub_opcion1 == 4 :
                print("LISTANDO LIBROS...")
                # Aquí iría el código para listar los libros
            elif sub_opcion1 == 0 :
                break
        # Aquí iría el código para añadir un libro

        elif opcion == 2 :
            print("ELIMINANDO LIBRO...")
        # Aquí iría el código para eliminar un libro
        elif opcion == 3:
            print("BUSCANDO LIBRO...")
        # Aquí iría el código para buscar un libro
        elif opcion == 4 :
            print("LISTANDO LIBROS...")
        # Aquí iría el código para listar los libros
        elif opcion == 5 :
            print("SALIENDO DE LA BIBLIOTECA...")
        elif opcion == 6 :
            print("LISTANDO LIBROS PRESTADOS...")
        # Aquí iría el código para listar los libros prestados
        elif opcion == 0:
            print("SALIENDO DEL PROGRAMA...")
        break
    else:
            print("OPCIÓN INVÁLIDA. POR FAVOR, INTENTE DE NUEVO.")