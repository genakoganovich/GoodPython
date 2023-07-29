import sympy
list(map(lambda x: print(x, end=' '), filter(lambda x: sympy.isprime(x), range(2, int(input())))))
