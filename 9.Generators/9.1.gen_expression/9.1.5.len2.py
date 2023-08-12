from string import ascii_lowercase
len2_gen = (a + b for a in ascii_lowercase for b in ascii_lowercase)
list(map(lambda _: print(next(len2_gen), end=' '), range(50)))
