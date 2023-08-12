def add_tag(tag):
    def add_parameter(s):
        return f'<{tag}>{s}</{tag}>'

    return add_parameter


add_tag_f = add_tag(input())
print(add_tag_f(input()))
