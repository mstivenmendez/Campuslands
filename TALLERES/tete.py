
 for libro in archivo_mayor["libros"]:
        if libro["codigo"] == codigo_libro:
            print(f"Libro encontrado: su codigo es:  {libro['codigo']} su nombre es: {libro['titulo']}")
            espacio()
            libro["titulo"] = validar_texto(f"Ingrese el nuevo título del libro:  \n")
            libro["autor"] = validar_texto(f"Ingrese el nuevo autor del libro:  \n")
            libro["editorial"] = validar_texto(f"Ingrese la nueva editorial del libro:  \n")
            print("Libro actualizado exitosamente.")
            espacio()
            return