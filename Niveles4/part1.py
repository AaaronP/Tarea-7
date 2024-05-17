def aux(T, n, levels, level):
    if not T:
        return

    node, left, right = T

    if node == n:
        levels.append(level)

    aux(left, n, levels, level + 1)
    aux(right, n, levels, level + 1)


def levels(T, n):
    if not T:
        return []

    levels = []

    aux(T, n, levels, 0)
    return levels
