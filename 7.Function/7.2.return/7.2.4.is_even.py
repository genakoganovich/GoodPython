def is_even(n):
    return not n % 2


while True:
    m = int(input())
    if m == 1:
        break
    if is_even(m):
        print(m)
