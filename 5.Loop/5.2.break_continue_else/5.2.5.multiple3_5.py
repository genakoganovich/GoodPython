n = int(input())

if n < 100:
    print(*[x for x in range(1, n + 1) if not x % 15])
else:
    print('слишком большое значение n')
