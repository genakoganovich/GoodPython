def is_free(lst):
    return any(x == '#' for row in lst for x in row )
