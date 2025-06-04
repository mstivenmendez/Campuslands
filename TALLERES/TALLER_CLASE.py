import csv
import json
import os

def leerJson(path: str):
    with open(path, mode='r') as file:
        datos = json.load(file)
        return datos
    
def escribirJson(path: str, data: list):
    with open(path,mode= 'w') as file:
        json.dump(data, file, indent= 2)


def espacio():
    print("\n")

def validacion_ingreso_sub_menu_principal(mensaje: str, valorminimo: int = 0, valormaximo: int = 6):


    # Función para validar el ingreso de datos
    while True:
        try:
            valor = int(input(mensaje))
            if valorminimo <= valor <= valormaximo:
                return valor
            else:
                print(f"POR FAVOR INGRESE VALORES ENTRE {valorminimo} y {valormaximo}.")

        except:
            print("Entrada no válida. Por favor, ingrese un número entero.")

def mostrar_menu_principal():
    espacio()
    print("----- MENÚ PRINCIPAL -----")
    print("1. Leer y mostrar un archivo de texto línea a línea")
    print("2. Sobrescribir un archivo de texto y luego añadir contenido")
    print("3. Crear un CSV de usuarios y leerlo")
    print("4. Actualizar un CSV (lectura-escritura)")
    print("5. Leer y escribir JSON de productos")
    print("6. Convertir CSV a JSON")
    print("7. Manejo de excepciones en concatenación de (str + int)")
    print("0. Salir")      

def leerArchivo(ingreso: str,mode="r") -> list:
    try:
        with open(ingreso, mode=mode) as leerarchivo:
            return leerarchivo.readlines()
    except FileNotFoundError as e:
        print(f"El archivo {ingreso} no existe. Por favor, verifique la ruta.\nError: {e}")
        return []

def validar_texto(texto: str):
    while True:
        valor = input(texto)
        if valor.isalpha():
            return valor
        else:
            print("Entrada no válida. Por favor, ingrese solo texto.")

#  with open('archivo_csv.csv', 'r', encoding='utf-8') as csv_file, \
#         open('archivo_json.json', 'w', encoding='utf-8') as json_file:
#     csv_reader = csv.DictReader(csv_file)
#     datos = list(csv_reader)
#     json_string = json.dumps(datos, indent=4)
#     json_file.write(json_string)           

def leerArchivoCSV(ingreso: str) -> list:
    with open(ingreso, mode= 'r', newline='') as leerarchivocsv:
        filas = csv.DictReader(leerarchivocsv)
        return list(filas)

def escribirArchivo(ingreso: str, listas: list, mode = 'a'):
    with open(ingreso, mode=mode) as escrituraarchivo:
        escrituraarchivo.writelines(listas)

def escribirArchivoCSV(ingreso: str, lineas: list, encabezados: list, mode = 'w'):
    try:
        with open(ingreso, mode=mode, newline= '') as escribirarchivo:
            loingresado = csv.DictWriter(escribirarchivo, fieldnames=encabezados)
            loingresado.writeheader()
            loingresado.writerows(lineas)
    except FileNotFoundError as e:
        print(f"El archivo {ingreso} no existe. Por favor, verifique la ruta.\nError: {e}")
        return []

diccionario_usuarios = [
    {"id": 1, "nombre": "Juan", "ciudad": "Bogotá"},
    {"id": 2, "nombre": "Ana", "ciudad": "Medellín"},
    {"id": 3, "nombre": "Luis", "ciudad": "Cali"},
    {"id": 4, "nombre": "María", "ciudad": "Bogotá"},
    {"id": 5, "nombre": "Pedro", "ciudad": "Barranquilla"}
]

def actualizarCSV(ingreso: str):
    opcion = validacion_ingreso_sub_menu_principal("Ingrese el ID del usuario a modificar: ", 1, 5)

    try:
        usuarios = leerArchivoCSV(ingreso)
        for usuario in usuarios:
            if int(usuario['id']) == opcion:
                nueva_ciudad = validar_texto("Ingrese la nueva ciudad: ")
                usuario['ciudad'] = nueva_ciudad
                break
        else:
            print(f"No se encontró el usuario con ID {opcion}.")
        
        escribirArchivoCSV(ingreso, usuarios, ["id", "nombre", "ciudad"], mode='w')
        print("CSV actualizado correctamente.")

    except FileNotFoundError as e:
        print(f"El archivo {ingreso} no existe. Por favor, verifique la ruta.\nError: {e}")

while True:

    mostrar_menu_principal()
    opcion = validacion_ingreso_sub_menu_principal("Ingrese una opción: ", 0, 7)

    if opcion == 1:
        print("Leer y mostrar un archivo de texto línea a línea")
        espacio
        print("Contenido del archivo archivo.txt:")
        espacio()
        lineas = leerArchivo("archivo.txt", "r")
        for i, linea in enumerate(lineas, start=1):
            print(f"{i}: {linea.strip()}")

    elif opcion == 2:
        print("Sobrescribir un archivo de texto y luego añadir contenido")
        espacio
        escribirArchivo("diario.txt", ["Fecha: 2025-06-02\n"], mode='w')
        espacio()
        escribirArchivo("diario.txt", ["Actividad 1: Estudiar Python\n", "Actividad 2: Hacer ejercicio\n"], mode='a')
        espacio()
        print("Contenido del archivo diario.txt:")
        espacio()
        lineas_diario = leerArchivo("diario.txt", "r")
        for linea in lineas_diario:
            print(linea.strip())

        
    elif opcion == 3:
        print("Crear un CSV de usuarios y leerlo")
        espacio()
        encabezados = ["id", "nombre", "ciudad"]
        escribirArchivoCSV("usuarios.csv", diccionario_usuarios, encabezados, mode='w')
        print("Contenido del archivo usuarios.csv:")
        espacio()
        usuarios = leerArchivoCSV("usuarios.csv")
        opcion = validar_texto("Ingrese la ciudad para filtrar usuarios (ej. Bogotá): ")
        espacio()
        for usuario in usuarios:
            if usuario['ciudad'] == opcion:
                print(usuario)
       
    elif opcion == 4:
        print("Actualizar un CSV (lectura-escritura")
        espacio()
        actualizarCSV("usuarios.csv")

        
    elif opcion == 5 :
        print("Leer y escribir JSON de productos*")
        for producto in leerJson("productos.json"):
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}")
        espacio()
        
        ingreso_producto = {
            "id": 4,
            "nombre": "durazno",
            "precio": 1500
        }
        print("Contenido del archivo productos.json:")
        espacio()
        ingreso = leerJson("productos.json")
        ingreso.append(ingreso_producto)
        escribirJson("productos.json", ingreso)
        for producto in leerJson("productos.json"):
            print(f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}")
      
        
       
    elif opcion == 6:
        print("Convertir CSV a JSON**")
        espacio()
        cvsd = leerArchivoCSV("usuarios.csv")
        escribirJson("usuarios.json", cvsd)

        
    elif opcion == 7 :
        print("Manejo de excepciones en concatenación de (str + int)")
        espacio()
        try:
            nombre = validar_texto("Ingrese su nombre: ")
            numero = int(input("Ingrese un número: "))  # Intenta convertir la entrada a entero
            print(f"El número es:", numero, "y su nombre es:", nombre)
        except ValueError:
            print("Entrada inválida. Debe ingresar un número válido.")

    elif opcion == 0:
        print("Saliendo del programa...")
        break
        print("Opción no válida. Por favor, intente de nuevo.")