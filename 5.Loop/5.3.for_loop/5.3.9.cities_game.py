cities = list(map(lambda x: str(x).lower(), input().split()))

result = 'НЕТ'
prev = cities[0]
for city in cities[1:]:
    last = prev[~0] if prev[~0] not in 'ьъы' else prev[~1]
    if last != city[0]:
        break
    prev = city
else:
    result = 'ДА'
print(result)
