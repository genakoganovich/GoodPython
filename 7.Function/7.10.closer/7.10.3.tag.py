def add_tag():
    def add_h1(s):
        return f'<h1>{s}</h1>'

    return add_h1


add_tag_f = add_tag()
print(add_tag_f(input()))
