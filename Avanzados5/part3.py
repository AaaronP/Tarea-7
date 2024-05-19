def generar(i, e):
    T = []

    if i > e:
        T.append([])
        return T

    for j in range(i, e + 1):
        leftT = generar(i, j - 1)
        rightT = generar(j + 1, e)

        for l in leftT:
            for r in rightT:
                rot = [j, l, r]
                T.append(rot)
    return T


def generarArbol(n):
    if n == 0:
        return [[]]
    return generar(1, n)
