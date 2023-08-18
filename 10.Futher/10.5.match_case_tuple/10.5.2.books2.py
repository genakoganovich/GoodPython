t = (int, str, str, float, int)
book = [t[i](x) if t[i] != str else x.strip() for i, x in enumerate(input().split(","))]
match book:
    case [_, str(author), str(title)] if len(author) > 5 and len(title) > 9:
        print('Yes')
    case [_, str(author), str(title), float(price)] if len(author) > 5 and price > 0:
        print('Yes')
    case [_, str(author), str(title), int(year)] if year > 2019:
        print('Yes')
    case [_, str(author), str(title), float(price), int(year)] if price > 0 and year > 2019:
        print('Yes')
    case _:
        print('No')
