def show_menu(func):
    def wrapper(*args, **kwargs):
        res = sorted(func(*args, **kwargs))
        return res

    return wrapper


@show_menu
def get_list(s):
    return list(map(int, str(s).split()))


print(*get_list(input()))
