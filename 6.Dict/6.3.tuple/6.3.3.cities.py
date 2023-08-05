t = tuple(input().split())
t = tuple(v for v in t if v != 'Ульяновск')
print(*t)