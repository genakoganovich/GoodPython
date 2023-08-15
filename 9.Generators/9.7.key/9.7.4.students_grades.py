import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
columns = 'Имя;Зачет;Оценка;Номер'.split(';')
t = tuple(tuple(map(lambda x: int(x) if str(x).isdigit() else x, str(s).split(';'))) for s in lst_in)
t_sorted = tuple(
    tuple(sorted(t[i], key=lambda x: columns.index(t[0][t[i].index(x)]))
          )
    for i in range(len(t))
)
