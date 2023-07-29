import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
result = 'НЕТ'
break_out_flag = False
for i in range(len(lst_in) - 1):
    for j in range(len(lst_in) - 1):
        if [lst_in[x][y] for x in range(i, i + 2) for y in range(j, j + 2)].count(1) > 1:
            break_out_flag = True
            break
    if break_out_flag:
        break
else:
    result = 'ДА'
print(result)
