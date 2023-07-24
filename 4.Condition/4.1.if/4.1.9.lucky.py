digits = list(map(int, input()))
print('ДА' if sum(digits[0:3]) == sum(digits[3:]) else 'НЕТ')
