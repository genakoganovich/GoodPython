# ввод значений a и b (переменные a и b не менять!)
a, b = map(int, input().split())

# здесь продолжайте программу
abs_gen = (abs(x) for x in range(a, b + 1))
list(map(lambda _: print(next(abs_gen)), range(5)))