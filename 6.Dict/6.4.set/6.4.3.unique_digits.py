result = sorted(set(filter(str.isdigit, input())))
if result:
    print(*result)
else:
    print('НЕТ')
