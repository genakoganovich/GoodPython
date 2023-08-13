import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
list(map(lambda x: print(*x), zip(*[str(s).split() for s in lst_in])))
