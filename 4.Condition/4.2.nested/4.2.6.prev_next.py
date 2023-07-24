import datetime
from datetime import date
m, n = map(int, input().split())
prev_day = date(2002, m, n) - datetime.timedelta(days=1)
next_day = date(2002, m, n) + datetime.timedelta(days=1)

print(f'{prev_day.month:02}.{prev_day.day:02} {next_day.month:02}.{next_day.day:02}')
