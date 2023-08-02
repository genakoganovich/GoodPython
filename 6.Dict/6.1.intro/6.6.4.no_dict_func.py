import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список lst_in)
d = {key_value[0]: key_value[1] for
     key_value in [[int(s[0]), s[1]] for s in [str(x).split('=') for x in lst_in]]}
print(*sorted(d.items()))
