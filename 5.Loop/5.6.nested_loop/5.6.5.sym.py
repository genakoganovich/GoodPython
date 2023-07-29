import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

result = 'НЕТ'
# здесь продолжайте программу (используйте список lst_in)
break_out_flag = False
for i in range(len(lst_in)):
    for j in range(i + 1, len(lst_in[0])):
        if lst_in[i][j] != lst_in[j][i]:
            break_out_flag = True
            break
    if break_out_flag:
        break
else:
    result = 'ДА'
print(result)
