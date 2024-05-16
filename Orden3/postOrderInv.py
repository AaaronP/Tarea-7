def postOrderInv(T):
    if not T:
        return []

    v, L, R = T

    return postOrderInv(R) + postOrderInv(L) + [v]
