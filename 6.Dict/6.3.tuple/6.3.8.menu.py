import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
menu = tuple([tuple(str(s).split()) for s in lst_in])
print(menu)
