key = 123
print(''.join(map(lambda x: chr(ord(x) ^ key), input())))
