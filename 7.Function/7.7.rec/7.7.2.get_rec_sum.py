def get_rec_sum(lst):
    return 0 if not len(lst) else lst[0] + get_rec_sum(lst[1:])


print(get_rec_sum(list(map(int, input().split()))))
