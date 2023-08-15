import sys

# считывание списка из входного потока (не меняйте переменную lst_in в программе)
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу (используйте список строк lst_in)
order = "Имя;Зачет;Оценка;Номер"
t = tuple(tuple(int(st) if st.isdigit() else st for st in row.split(";")) for row in lst_in)
t_sorted = tuple(zip(*sorted(list(zip(*t)), key=lambda x: order.find(x[0]))))