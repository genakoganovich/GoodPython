def counter_add(n):
    def add_n(value):
        return value + n

    return add_n


cnt = counter_add(2)
k = int(input())
print(cnt(k))
