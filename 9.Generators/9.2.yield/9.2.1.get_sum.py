# ввод значения N (эту переменную не менять)
N = int(input())


# здесь продолжайте программу
def get_sum(n):
    res = 0
    for i in range(1, n + 1):
        res += i
        yield res


d = get_sum(N)
list(map(lambda _: print(next(d), end=' '), range(1, N + 1)))
