d = filter(lambda x: len(x) > 5, input().split())
list(map(lambda _: print(next(d), end=' '), range(3)))
