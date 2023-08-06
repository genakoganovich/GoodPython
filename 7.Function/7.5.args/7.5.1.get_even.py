def get_even(*args):
    return [x for x in args if x % 2 == 0]


print(*get_even(*list(map(int,input().split()))))
