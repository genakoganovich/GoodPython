def filter_lst(it, key=None):
    if key is None:
        return tuple(it)

    res = ()
    for x in it:
        if key(x):
            res += (x,)

    return res


# здесь продолжайте программу
input_lst = list(map(int, input().split()))
print(*filter_lst(input_lst))
print(*filter_lst(input_lst, lambda x: x < 0))
print(*filter_lst(input_lst, lambda x: x >= 0))
print(*filter_lst(input_lst, lambda x: x in range(3, 6)))
