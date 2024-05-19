def find(rutas, nodo, aNivel, ruta, nivel):
    if aNivel == nivel:
        rutas.append(ruta)

    if aNivel < nivel:
        for i in nodo[1]:
            find(rutas, i, aNivel + 1, ruta + [i[0]], nivel)


# Arbol enario
def rutasNivel(T, nivel):
    rutas = []
    if not T:
        return rutas

    find(rutas, T, 0, [T[0]], nivel)
    return rutas
