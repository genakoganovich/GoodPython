numbers = list(map(int, input().split()))

for i in range(1, len(numbers)):
    for j in range(len(numbers) - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
print(*numbers)
