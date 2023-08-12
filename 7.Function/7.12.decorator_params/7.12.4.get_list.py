from functools import wraps


def get_sum(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sum(res)

    return wrapper


@get_sum
def get_list(s):
    """Функция для формирования списка целых значений"""
    return list(map(int, str(s).split()))
