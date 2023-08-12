def func_show(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {res}")
        return res

    return wrapper


def get_sq(width, height):
    return width * height
