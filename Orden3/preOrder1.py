def preOrder(T):
    if not T:
        return []

    v, L, R = T

    return [v] + preOrder(L) + preOrder(R)
