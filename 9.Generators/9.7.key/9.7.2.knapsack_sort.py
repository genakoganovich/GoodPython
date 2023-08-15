import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
d = dict(s.split("=") for s in lst_in)
print(*sorted(d, key=lambda x: int(d.get(x)), reverse=True))
