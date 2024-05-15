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


def maxValue(T):
    if T == []:
        return -1

    v, h = T

    if h == []:
        return v

    mx = v
    for hjs in h:
        mx = max(mx, maxValue(hjs))
    return mx


def rutaMayor(T):
    return ruta(T, maxValue(T))
