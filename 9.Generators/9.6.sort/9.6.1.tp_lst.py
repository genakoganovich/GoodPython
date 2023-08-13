# ввод строки в переменную s (переменную в программе не менять)
s = input()

# здесь продолжайте писать программу
lst = list(map(int, s.split()))
tp_lst = tuple(sorted(tuple(lst)))
lst.sort()
