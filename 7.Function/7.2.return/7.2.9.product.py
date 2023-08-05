def get_product(a, b):
    return a * b


numbers = list(map(int, input().split()))
print(get_product(min(numbers), max(numbers)))
