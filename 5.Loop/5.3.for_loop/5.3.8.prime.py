n = int(input())
print('ДА' if all(n % i for i in range(2, n)) else 'НЕТ')
