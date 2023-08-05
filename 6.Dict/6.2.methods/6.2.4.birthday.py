import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = dict()
for s in lst_in:
    x, y = s.split()
    d.setdefault(x, []).append(y)

list(map(lambda z: print(f'{z[0]}: {", ".join(z[1])}'), d.items()))
