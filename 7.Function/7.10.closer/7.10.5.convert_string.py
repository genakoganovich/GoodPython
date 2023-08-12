def convert_string(tp):
    def convert(s):
        return list(map(int, str(s).split())) if tp == 'list' else tuple(map(int, str(s).split()))

    return convert


convert_string_f = convert_string(input())
print(convert_string_f(input()))
