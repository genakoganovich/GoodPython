from functools import wraps


def put_tag_param(tag='h1'):
    def put_tag(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return f'<{tag}>{res}</{tag}>'

        return wrapper

    return put_tag


@put_tag_param(tag='div')
def string_to_lower(s):
    return str(s).lower()


print(string_to_lower(input()))
