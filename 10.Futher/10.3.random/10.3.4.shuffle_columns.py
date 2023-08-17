import sys
import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

# здесь продолжайте программу
lst_t = list(zip(*list(map(str.split, lst_in))))
random.shuffle(lst_t)
list(map(lambda x: print(*x), list(zip(*lst_t))))
