def maxValue(T):
    if T == []:
        return -1

    v, h = T

    if h == []:
        return v

    mx = v
    for hjs in h:
        mx = max(mx, maxValue(hjs))
    return mx
