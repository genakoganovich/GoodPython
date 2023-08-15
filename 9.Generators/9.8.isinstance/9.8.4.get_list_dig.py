def get_list_dig(lst):
    return list(filter(lambda x: type(x) in [int, float], lst))
