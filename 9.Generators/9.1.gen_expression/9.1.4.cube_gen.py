a = int(input())
abs_gen = (abs(x) for x in range(-a, a + 1))
cube_gen = (x ** 3 for x in abs_gen)
list(map(lambda _: print(next(cube_gen), end=' '), range(4)))
