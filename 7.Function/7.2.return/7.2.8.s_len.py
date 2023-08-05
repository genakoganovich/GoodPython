def get_s_len(s):
    return s, len(s)


d = dict([get_s_len(s) for s in input().split()])
a = sorted(d, key=lambda x: d[x])
print(*a)
