def get_path(n):
    if n == 1:
        return 1
    if n == 2:
        return get_path(n - 1) + 1
    return get_path(n - 2) + get_path(n - 1)


print(get_path(int(input())))
