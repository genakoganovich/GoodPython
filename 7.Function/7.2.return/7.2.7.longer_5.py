def longer_5(s):
    return len(s) > 5


print(*[x for x in input().split() if longer_5(x)])
