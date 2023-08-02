import math

d = dict()

while True:
    n = int(input())
    if not n:
        break
    if n not in d:
        d[n] = round(math.sqrt(n), 2)
        print(d[n])
    else:
        print(f'значение из кэша: {d[n]}')
