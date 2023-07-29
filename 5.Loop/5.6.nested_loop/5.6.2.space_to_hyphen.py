import sys, re

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
list(map(lambda s: print(re.sub(r'\s+', '-', s)), lst_in))
