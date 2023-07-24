import datetime
from datetime import date
k = int(input())
days_of_week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
print(days_of_week[((date(2018, 1, 1) + datetime.timedelta(days=(k - 1))).weekday())])
