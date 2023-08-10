# ввод числа n
n = int(input())


# здесь задается функция fact_rec  (переменную n не менять!)
def fact_rec(n):
    if not n:
        return 1
    return fact_rec(n - 1) * n


print(fact_rec(n))
