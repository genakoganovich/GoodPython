def get_even_sum(it):
    return sum(filter(lambda x: type(x) == int and not x % 2, it))
