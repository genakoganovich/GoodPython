x = int(input())
start = 10
factor = 1.1

i = 1
while start <= x:
    start *= factor
    i += 1

print(i)
