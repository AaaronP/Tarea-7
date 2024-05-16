def inOrder(T):
    if not T:
        return []

    v, L, R = T

    return inOrder(L) + [v] + inOrder(R)
