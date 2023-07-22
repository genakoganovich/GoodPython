lst = list(map(int, input().split()))
lst[-1] = bool(lst[-1] % 2)
print(*lst)