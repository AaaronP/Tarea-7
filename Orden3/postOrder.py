def postOrder(T):
    if not T:
        return []

    v, L, R = T

    return postOrder(L) + postOrder(R) + [v]
