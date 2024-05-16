def nivel(T, n, current_level=0):
    if not T:
        return []

    v, left, right = T

    if n == v:
        return [current_level]

    level_left = nivel(left, n, current_level + 1)
    level_right = nivel(right, n, current_level + 1)

    if level_left:
        return level_left
    elif level_right:
        return level_right
    else:
        return []
    
print(nivel([50, [25, [15, [5, [5, [],[]],[]], []], []], [75, [5, [], []], []]], 5))