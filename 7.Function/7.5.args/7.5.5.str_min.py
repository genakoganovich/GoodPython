def str_min(x, y):
    return min(x, y)


def str_min3(x, y, z):
    return min(x, min(y, z))


def str_min4(w, x, y, z):
    return str_min(w, str_min3(x, y, z))
