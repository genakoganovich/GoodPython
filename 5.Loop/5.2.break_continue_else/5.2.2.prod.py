prod = 1

while True:
    n = int(input())
    if n < 0:
        continue
    if n > 0:
        prod *= n
    if n == 0:
        break
print(prod)
