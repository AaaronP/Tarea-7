def inOrderInv(T):
    if not T:
        return []

    v, L, R = T

    return inOrderInv(R) + [v] + inOrderInv(L)
