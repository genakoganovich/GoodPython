def fib_rec(n, f=[]):
    if n == 1:
        f.append(1)
        return f
    if n == 2:
        fib_rec(1, f).append(1)
        return f

    fib_rec(n - 1, f).append(f[-2] + f[-1])
    return f


# ввод числа N
N = int(input())

# здесь задается функция fib_rec (переменную N не менять!)
print(*fib_rec(N))
