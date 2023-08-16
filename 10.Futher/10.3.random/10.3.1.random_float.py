import random
# установка "зерна" датчика случайных чисел, чтобы получались одни и те же случайные величины
random.seed(1)

# здесь продолжайте программу
a, b = map(int, input().split())
print(round(a + random.random() * (b - a), 2))
