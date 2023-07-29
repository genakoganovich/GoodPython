n = int(input())
count = 1
i = 1
while i <= n:
    if not i % 3:
        count *= 2
    i += 1

print(count)
