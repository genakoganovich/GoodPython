import random
from string import ascii_lowercase, ascii_uppercase

# установка зерна датчика случайных чисел (не менять)
random.seed(1)

# здесь продолжайте программу
chars = ascii_lowercase + ascii_uppercase + "0123456789!?@#$*"
length = len(chars)


def pass_gen(n):
    while True:
        yield ''.join(chars[random.randint(0, length)] for _ in range(n))


d= pass_gen(int(input()))
list(map(lambda _: print(next(d)), range(5)))
