import re

print(*filter(lambda x: re.match(r'[A-Za-z0-9_]+@[A-Za-z0-9_]+.[A-Za-z0-9_]+', x), input().split()))
