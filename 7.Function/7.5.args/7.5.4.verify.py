def is_isolate(*tple):
    return tple.count(1) <= 1


def verify(inpt):
    for i in range(len(inpt) - 1):
        for j in range(len(inpt[i]) - 1):
            if not is_isolate(inpt[i][j], inpt[i][j+1], inpt[i+1][j], inpt[i+1][j+1]):
                return False
    return True


# Пример ввода
input_table = [
    [1, 0, 1],
    [0, 1, 1],
    [1, 0, 1]
]

# Вызываем функцию verify и выводим результат
print(verify(input_table))
