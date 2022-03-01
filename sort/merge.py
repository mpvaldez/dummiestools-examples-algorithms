# Esto ordena los datos partiendo en pequeñas listas y empezar a juntarlas ordenadas


def Merge(l1, l2):
    l3 = []
    while len(l1) > 0 and len(l2) > 0:
        if l1[0] < l2[0]:
            l3.append(l1[0])
            l1 = l1[1:]
        else:
            l3.append(l2[0])
            l2 = l2[1:]

    if len(l1) > 0:
        l3 = l3 + l1

    if len(l2) > 0:
        l3 = l3 + l2

    return l3


def MergeSort(listarda):
    # Caso base
    if len(listarda) == 1:
        return listarda

    # Caso recursivo
    li = listarda[: len(listarda) // 2]  # Lista izquierda
    ld = listarda[len(listarda) // 2 :]  # Lista derecha

    li = MergeSort(li)  # Recursividad para la de la izquierda
    ld = MergeSort(ld)  # Recursividad para la de la derecha

    return Merge(li, ld)


lista = [3, 8, -1, -10000, 25, 13, 15, 2, 15, 16, 99, 0, 5, -8, 10000, -85, 961, -961]

print(lista)

print(MergeSort(lista))
