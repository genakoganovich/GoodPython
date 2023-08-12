from functools import wraps


def sum_string_param(start):
    def sum_string_start(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res + start

        return wrapper

    return sum_string_start


@sum_string_param(start=5)
def sum_string(s):
    return sum(list(map(int, str(s).split())))


print(sum_string(input()))
