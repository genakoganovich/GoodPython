d = dict([str(s).split('=') for s in input().split()])
print(*sorted(d.items()))
