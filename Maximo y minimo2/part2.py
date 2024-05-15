def minValue(T):
    if T == []:
        return -1

    v, h = T

    if h == []:
        return v

    mx = v
    for hjs in h:
        mx = min(mx, minValue(hjs))
    return mx
