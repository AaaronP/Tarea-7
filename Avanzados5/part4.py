def generarArbolAltura(i, h):
    T = []
    if h == 0:
        T.append([])
        return T

    for j in range(i, h + 1):
        leftT = generarArbolAltura(i, j - 1)
        rightT = generarArbolAltura(i, h - i)

        for l in leftT:
            for r in rightT:
                rot = [j, l, r]
                T.append(rot)
    return T


def generarArboles(h):
    if h == 0:
        return [[]]
    return generarArbolAltura(1, h)
