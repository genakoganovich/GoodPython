names = input().split()

i = 0
result = 'ДА'
while i < len(names):
    if names[i][0].lower() == names[i][~0].lower():
        break
    i += 1
else:
    result = 'НЕТ'

print(result)
