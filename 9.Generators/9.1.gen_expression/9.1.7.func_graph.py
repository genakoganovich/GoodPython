a, b = map(int, input().split())

step = 0.01


def f(x):
    return 0.5 * pow(x, 2) - 2.0


x_gen = (a + i * step for i in range(0, b * int((1 / step)) + 1))
func_gen = (f(x) for x in x_gen)
list(map(lambda _: print(round(next(func_gen), 2), end=' '), range(20)))
