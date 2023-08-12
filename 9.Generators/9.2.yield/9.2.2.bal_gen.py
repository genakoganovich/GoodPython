def bal_gen(n):
    a = b = c = 1
    for i in range(n):
        if i > 2:
            a, b, c = b, c, a + b + c
        yield c


N = int(input())
d = bal_gen(N)
list(map(lambda _: print(next(d), end=' '), range(1, N + 1)))
