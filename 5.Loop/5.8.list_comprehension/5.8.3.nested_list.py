n = int(input())
matrix = [[(0, 1)[i == j] for j in range(n)] for i in range(n)]
list(map(lambda row: print(*row), matrix))
