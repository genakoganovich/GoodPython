def print_min_max_sum(numbers):
    print(f"Min = {min(numbers)}, max = {max(numbers)}, sum = {sum(numbers)}")


print_min_max_sum(list(map(int, input().split())))
