def fib_sequence(n):
    a = b = 1
    for i in range(n):
        if i > 1:
            a, b = b, a + b
        yield b


for x in fib_sequence(int(input())):
    print(x, end=' ')
