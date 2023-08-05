numbers = tuple(map(int, input().split()))
print(*filter(lambda i: numbers.count(numbers[i]) > 1, range(len(numbers))))
