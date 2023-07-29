import math
numbers = list(map(int, input().split()))
n = int(math.sqrt(len(numbers)))
print([numbers[i:i + n] for i in range(0, len(numbers), n)])
