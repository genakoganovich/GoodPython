import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
# здесь продолжайте программу (используйте список lst_in и menu)
d = dict([str(s).split('=') for s in lst_in])
menu = {**menu, **d}
