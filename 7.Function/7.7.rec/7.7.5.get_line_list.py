d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]


# здесь продолжайте программу
def get_line_list(lst, a=[]):
    if not isinstance(lst, list):
        a.append(lst)
        return a
    for x in lst:
        get_line_list(x, a)
    return a


print(get_line_list(d))
