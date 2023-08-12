from functools import wraps
import re

t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}


def put_tag_param(chars='!?'):
    def put_tag(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            res = re.sub(fr'[{chars}]', '-', res)
            res = re.sub(r'-+', '-', res)
            return res

        return wrapper

    return put_tag


@put_tag_param(chars="?!:;,. ")
def translate(s):
    return ''.join([t[c] if c in t else c for c in s])


print(translate(input().lower()))
