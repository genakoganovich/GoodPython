import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
tp = tuple(map(lambda x: tuple(x.split('=')), lst_in))
list(map(lambda x: print(x[0], end=' '), filter(lambda x: int(x[1]) >= 500, tp)))
