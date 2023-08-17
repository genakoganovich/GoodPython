N = 10
P = [[0] * N for i in range(N)]
i = j = 0

if i == 0:
    i += 1
if i == 9:
    i -= 1
if j == 0:
    j += 1
if j == 9:
    j -= 1

print([row[j - 1: j + 2] for row in P[i - 1: i + 2]])
