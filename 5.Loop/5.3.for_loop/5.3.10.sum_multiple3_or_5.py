n = int(input())
print(sum(filter(lambda x: not (x % 3 and x % 5), range(1, n))))
