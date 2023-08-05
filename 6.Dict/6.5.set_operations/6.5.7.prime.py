prime_numbers = [2, 3, 5, 7]
setA = {2, 3, 5}
n = int(input())
setB = set([m for m in prime_numbers if not n % m])
print('ДА' if setA <= setB else 'НЕТ')
