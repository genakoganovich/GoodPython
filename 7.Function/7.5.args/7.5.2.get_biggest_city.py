def get_biggest_city(*args):
    city_len = [len(c) for c in args]
    return args[city_len.index(max(city_len))]


print(get_biggest_city(*input().split()))
