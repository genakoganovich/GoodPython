def counter_add():
    def add_5(value):
        return value + 5

    return add_5


cnt = counter_add()
k = int(input())
print(cnt(k))
