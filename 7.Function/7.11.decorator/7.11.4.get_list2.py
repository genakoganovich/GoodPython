def get_dict(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        res = dict(zip(res[0], res[1]))
        return res

    return wrapper


@get_dict
def get_list(lines):
    return [str(s).split() for s in lines]


d = get_list([input() for _ in range(2)])
print(*sorted(d.items()))
