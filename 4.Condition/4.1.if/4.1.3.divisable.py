m, n = map(int, input().split())
print(f'{m} на {n} нацело не делится' if m % n else m // n)
