def is_string(lst):
    return all(map(lambda x: type(x) == str, lst))
