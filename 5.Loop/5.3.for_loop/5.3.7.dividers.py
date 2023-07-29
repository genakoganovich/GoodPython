n = int(input())
list(map(lambda x: print(x), filter(lambda x: not n % x, range(1, n + 1))))
