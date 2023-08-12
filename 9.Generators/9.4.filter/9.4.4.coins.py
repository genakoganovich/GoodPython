coins = set(map(int, input().split())) & set(map(int, input().split()))
print(*sorted(filter(lambda x: not x % 2, coins)))
