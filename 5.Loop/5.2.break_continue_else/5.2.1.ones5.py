p = [0] * 10
count = 0

while count < 5:
    i = int(input())
    if p[i] == 0:
        p[i] = 1
        count += 1
print(*p)
