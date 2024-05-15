# def nivel(T, n):
#     if not T:
#         return -1

#     v, left, right = T

#     if n == v:
#         return 0

#     level_left = nivel(left, n)
#     level_right = nivel(right, n)

#     if level_left >= 0:
#         return level_left + 1
#     elif level_right >= 0:
#         return level_right + 1
#     else:
#         return -1
