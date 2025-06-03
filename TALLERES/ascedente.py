
numeros = [1, 42, 3, 14, 5, 6, 7,3 , 9, 80]
def ascendente(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista
print(ascendente(numeros))