def put_tag(text, tag='h1'):
    return f'<{tag}>{text}</{tag}>'


s = input()
print(put_tag(s))
print(put_tag(s, 'div'))
