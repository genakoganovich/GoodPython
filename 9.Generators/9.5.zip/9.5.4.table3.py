n = 3
s = input().split()
list(map(lambda x: print(*x), zip(*[iter(s)] * n)))
