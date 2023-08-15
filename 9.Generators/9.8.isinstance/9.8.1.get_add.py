def get_add(a, b):
    return a + b \
        if (all(type(x) == str for x in [a, b]) or all(type(x) in (int, float) for x in [a, b])) \
        else None
