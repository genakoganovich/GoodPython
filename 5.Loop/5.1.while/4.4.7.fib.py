a = b = 1
for i in range(int(input())):
    if i > 1:
        a, b = b, a + b
    print(b, end=' ')
