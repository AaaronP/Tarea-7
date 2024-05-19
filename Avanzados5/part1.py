def hojas(T):
    if not T:
        return []

    node = T[0]
    left = T[1]
    right = T[2]

    if not left and not right:
        return [node]

    list = []
    if left:
        list += hojas(T[1])
    if right:
        list += hojas(T[2])
    return list


def nivel(T, n):
    if not T:
        return -1

    v, left, right = T

    if n == v:
        return 0

    level_left = nivel(left, n)
    level_right = nivel(right, n)

    if level_left >= 0:
        return level_left + 1
    elif level_right >= 0:
        return level_right + 1
    else:
        return -1


# Arbol binario
def balanceado(T):
    hojs = hojas(T)

    list = []
    for h in hojs:
        list.append(nivel(T, h))

    mx = max(list)
    mi = min(list)

    if mx - mi > 1:
        return False
    return True
