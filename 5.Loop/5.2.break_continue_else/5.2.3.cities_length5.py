cities = input().split()
i = 0
result = 'НЕТ'
while i < len(cities):
    if len(cities[i]) <= 5:
        break
    i += 1
else:
    result = 'ДА'

print(result)
