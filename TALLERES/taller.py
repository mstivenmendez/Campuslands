
notas = []

def agregar_nota(nota):
    if isinstance(nota, (int, float)) and 0 <= nota <= 10:
        notas.append(nota)
    else:
        raise ValueError("La nota debe ser un número entre 0 y 10.")    