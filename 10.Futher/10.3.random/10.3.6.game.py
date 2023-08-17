import random

# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)
# начальная инициализация поля (переменные P и N не менять, единицы записывать в список P)
N = int(input())
P = [[0] * N for i in range(N)]


# здесь продолжайте программу
def fix(x, max_value):
    if x == 0:
        x += 1
    if x == max_value:
        x -= 1
    return x


def has_ones(m):
    return any(any(row) for row in m)


def run():
    count = 0
    M = 10
    while count < M:
        row = random.randint(0, N - 1)
        pos = random.randint(0, N - 1)

        i = fix(row, P)
        j = fix(pos, P)

        if not has_ones([row[j - 1: j + 2] for row in P[i - 1: i + 2]]):
            P[row][pos] = 1
            count += 1

    # list(map(lambda line: print(*line), P))
    # print(count)


run()
