n = int(input())

i = 0
deposit = 1000
# print(round(deposit * (1.05 ** n), 2))
while i < n:
    deposit *= 1.05
    i += 1
print(round(deposit, 2))

