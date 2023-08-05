import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
phone_name = [str(s).split() for s in lst_in]
d = dict([[s[1], [x[0] for x in phone_name if x[1] == s[1]]] for s in phone_name])
print(*sorted(d.items()))
