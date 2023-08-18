cmd = ("Балакирев С.М.", "Python", 2000.78)

match cmd:
    case tuple() as book:
        print(f"кортеж: {book}")
    case _:  # wildcard
        print("непонятный формат данных")


match cmd:
    case author, title, price:
        print(f"Книга: {author}, {title}, {price}")
    case _:  # wildcard
        print("непонятный формат данных")


# cmd = ("Балакирев С.М.", "Python", 2000.78, 2022)
match cmd:
    case author, title, price, *_:
        print(f"Книга: {author}, {title}, {price}")
    case _:  # wildcard
        print("непонятный формат данных")