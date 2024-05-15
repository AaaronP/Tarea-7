def altura(T):
    if T == []:
        return 0

    v, h = T

    if h == []:
        return 0
    mx = -1
    for hjs in h:
        mx = max(mx, altura(hjs) + 1)
    return mx
