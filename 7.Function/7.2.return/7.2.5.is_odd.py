def is_odd(n):
    return n % 2


print(*[x for x in input().split() if is_odd(int(x))])
