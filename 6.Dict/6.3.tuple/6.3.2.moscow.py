t = tuple(input().split())
if 'Москва' not in t:
    t += ('Москва',)
print(*t)
