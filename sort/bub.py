# Esto ordena los datos comparando uno por uno los elementos y cambiando su orden si es mas chico que el siguiente.
# Recorre muchas veces la lista


def BubbleSort(lista):
    n = len(lista)

    for i in range(1, n):
        for j in range(0, n - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
        print(lista)
        i += 1


lista = [3, 8, -1, -10000, 25, 13, 15, 2]

print(lista)

print(BubbleSort(lista))
