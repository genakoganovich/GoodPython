def is_prime(n):
    return all(n % m for m in range(2, n))


def prime_gen():
    i = 1
    while True:
        i += 1
        while not is_prime(i):
            i += 1
        yield i


d = prime_gen()
list(map(lambda _: print(next(d), end=' '), range(20)))
