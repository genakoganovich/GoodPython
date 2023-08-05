import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {i.split(': ')[0]: {j.split(': ')[1] for j in lst_in if i.split(': ')[0] == j.split(': ')[0]} for i in lst_in}
print(d)
