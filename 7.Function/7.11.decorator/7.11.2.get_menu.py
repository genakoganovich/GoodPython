def show_menu(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        for i, menu_item in enumerate(res, start=1):
            print(f'{i}. {menu_item}')
        return res

    return wrapper


@show_menu
def get_menu(s):
    return str(s).split()
