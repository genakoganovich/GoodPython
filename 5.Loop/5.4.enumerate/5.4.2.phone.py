import re

print('ДА' if re.match(r'\+7\(\d{3}\)\d{3}-\d{2}-\d{2}', input()) else 'НЕТ')
