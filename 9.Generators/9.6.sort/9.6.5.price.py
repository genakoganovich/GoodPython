import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))


# здесь продолжайте программу (используйте список строк lst_in)
def get_cheep_3(d):
    return [item[1] for item in sorted(d.items())][:3]


price = {int(s[1]): s[0] for s in [str(x).split(':') for x in lst_in]}
print(*get_cheep_3(price))
