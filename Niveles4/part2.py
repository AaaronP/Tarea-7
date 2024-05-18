def aux(T, cLevel, level, nodes):
    if not T:
        return

    node, left, right = T
    if cLevel == level:
        nodes.append(node)

    aux(left, cLevel + 1, level, nodes)
    aux(right, cLevel + 1, level, nodes)


def nodosLevel(T, level):
    if not T:
        return []

    nodes = []
    aux(T, 0, level, nodes)
    return nodes
