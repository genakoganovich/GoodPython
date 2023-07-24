a, b, c, d = map(int, input().split())
print('ДА' if min(a, b) > min(c, d) + 1 and max(a, b) > max(c, d) + 1 else 'НЕТ')
