# ввод строки (переменную s не менять)
s = input()
s_lst = s.split()

# здесь продолжайте программу
tp = tuple(map(lambda x: tuple(x.split('=')), s_lst))
