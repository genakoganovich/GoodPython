numbers = list(map(int, input().split()))
print(*filter(lambda x: len(str(abs(x))) == 2, numbers))
