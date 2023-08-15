import sys

# считывание списка из входного потока (переменную lst_in не менять)
lst_in = list(map(str.strip, sys.stdin.readlines()))
rank = 'рядовой, сержант, старшина, прапорщик, лейтенант, капитан, майор, подполковник, полковник'.split(', ')
# здесь продолжайте программу (используйте список строк lst_in)
lst = [str(s).split('=') for s in lst_in]
lst = sorted(lst, key=lambda x: rank.index(x[1]))
