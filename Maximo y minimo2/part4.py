def ruta(T, n):
    if not T:
        return []

    v, h = T

    if v == n:
        return [v]

    if not h:
        return []

    lista = [v]
    for i in h:
        camino = ruta(i, n)
        if camino:
            return lista + camino
    return []


def minValue(T):
    if T == []:
        return -1

    v, h = T

    if h == []:
        return v

    mx = v
    for hjs in h:
        mx = min(mx, minValue(hjs))
    return mx


def rutaMenor(T):
    return ruta(T, minValue(T))
