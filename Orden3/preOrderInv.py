def preOrderInv(T):
    if not T:
        return []

    v, L, R = T

    return [v] + preOrderInv(R) + preOrderInv(L)
