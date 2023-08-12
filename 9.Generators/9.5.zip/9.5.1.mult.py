a, b = (map(int, input().split()) for _ in range(2))
d = (i * j for i, j in zip(a, b))
list(map(lambda _: print(next(d), end=' '), range(3)))
