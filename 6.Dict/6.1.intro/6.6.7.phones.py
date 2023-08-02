phones = input().split()
d = dict([[x[:2], [y for y in phones if y[:2] == x[:2]]] for x in phones])
print(*sorted(d.items()))
