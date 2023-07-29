import sys

lst_in = list(map(str.strip, sys.stdin.readlines()))
print(*filter(lambda x: len(str(x).split()) < 2, lst_in))
