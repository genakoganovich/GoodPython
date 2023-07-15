book = [input() for _ in range(4)]
del book[2]
book[1] = "Пушкин"
book[2] = float(book[2]) * 2
print(book)
