d=dict([[i[0], int(i[1])] for i in [i.split('=') for i in input().split()]])
print(*sorted(d.items()))
