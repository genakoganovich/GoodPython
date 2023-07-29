numbers = list(map(int, input().split()))

for i in range(len(numbers)):
    min_value = min(numbers[i:])
    min_index = numbers.index(min_value, i)
    if i != min_index:
        numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

print(*numbers)
