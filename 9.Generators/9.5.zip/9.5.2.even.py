import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
# d = zip(*zip(*[line.split() for line in lst_in]))
d = zip(*zip(*lst_in))
list(map(lambda x: print(*x), d))
