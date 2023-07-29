it = iter(input())

while True:
    char = next(it)
    if char == ' ':
        break
    print(char, end='')
