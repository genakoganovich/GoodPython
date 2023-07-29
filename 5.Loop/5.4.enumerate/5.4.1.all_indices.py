s = input()
result = [i for i in range(len(s) - 1) if s[i:i + 2] == 'ра']

if result:
    print(*result)
else:
    print(-1)
