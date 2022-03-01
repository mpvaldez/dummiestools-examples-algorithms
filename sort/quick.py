# Esto parte la lista a traves de un pivot
# Recursivo: partir la nueva lista desde un nuevo pivot
# Luego ordenar desde las listas partidas con el pivot en el medio


def Quick(listarda):
    # Caso base
    if len(listarda) <= 1:
        return listarda

    # Caso recursivo
    pivote = listarda.pop()  # Elijo arbitrariamente el ultimo elemento

    li = []  # Lista izquierda, menores que el pivote
    ld = []  # Lista derecha, menores que el pivote

    for e in listarda:
        if e <= pivote:
            li.append(e)
        else:
            ld.append(e)

    # Entonces ordeno los lados
    li = Quick(li)
    ld = Quick(ld)

    return li + [pivote] + ld


lista = [3, 8, -1, -10000, 25, 13, 15, 2, 15, 16, 99, 0, 5, -8, 10000, -85, 961, -961]

print(lista)

print(Quick(lista))
