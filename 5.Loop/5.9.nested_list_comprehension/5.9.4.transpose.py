import sys

# считывание списка из входного потока
s = sys.stdin.readlines()
lst_in = [list(map(int, x.strip().split())) for x in s]

# здесь продолжайте программу (используйте список lst_in)
A = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
for row in A:
    print(*row)
