cities = set()

while True:
    c = input()
    if c == 'q':
        break
    cities.add(c)

print(len(cities))
