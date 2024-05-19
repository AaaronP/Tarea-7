# BFS
def anchura(T):
    if not T:
        return

    max = 0
    ancho = 0
    aNivel = 0
    cola = [(T, aNivel)]

    while cola:
        ancho = len(cola)
        if ancho > max:
            max = ancho
            mas_ancho = aNivel

        for i in range(ancho):
            n, nivel = cola.pop(0)

            _, left, right = n

            if left:
                cola.append((left, nivel + 1))
            if right:
                cola.append((left, nivel + 1))

        aNivel += 1
    return mas_ancho
