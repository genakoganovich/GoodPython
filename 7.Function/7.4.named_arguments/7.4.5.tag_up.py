def put_tag_up(text, tag='h1', up=True):
    if up:
        tag = tag.upper()
    return f'<{tag}>{text}</{tag}>'


s = input()

print(put_tag_up(s, 'div'))
print(put_tag_up(s, 'div', up=False))
