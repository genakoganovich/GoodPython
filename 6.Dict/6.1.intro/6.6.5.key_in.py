d = dict([s.split('=') for s in input().split()])
print('ДА' if all(x in d for x in ['house', 'True', '5']) else 'НЕТ')
