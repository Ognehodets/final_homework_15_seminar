# Напишите скрипт, который получает текущее время и дату, а затем выводит их в
# формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер
# недели в году

from datetime import datetime

# на занятиях говорили, что воскресенье - это 0, но при запуске выяснилось, что понедельник
WEEKDAYS = ("понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье")

qur_date = datetime.now()
print(qur_date.strftime('%Y-%m-%d %H:%M:%S'))

qur_weekday = datetime.now().weekday()
for i in range(len(WEEKDAYS)):
    if i == qur_weekday:
        qur_weekday_str = WEEKDAYS[i]
print(qur_weekday_str)

qur_week = 1
first_day_of_month = datetime(day=1, month=datetime.now().month, year=datetime.now().year)
if first_day_of_month.weekday() < qur_weekday:
    day_difference = qur_weekday - first_day_of_month.weekday()
    first_qur_day_of_month = datetime(day=(1 + day_difference), month=datetime.now().month, year=datetime.now().year)
    qur_week = 1
else:
    day_difference = qur_weekday - first_day_of_month.weekday() + len(WEEKDAYS)
    first_qur_day_of_month = datetime(day=(1 + day_difference), month=datetime.now().month, year=datetime.now().year)
    qur_week = 2
qur_week = int(qur_week + (qur_date.day - first_qur_day_of_month.day) / len(WEEKDAYS))
print(f"{qur_week}-я неделя")
