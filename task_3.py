# Напишите функцию, которая принимает количество дней от текущей даты и
# возвращает дату, которая наступит через указанное количество дней. Дополнительно,
# выведите эту дату в формате YYYY-MM-DD.

from datetime import datetime, timedelta


def calculate_date(day_interval):
    return (datetime.now() + timedelta(days=day_interval)).strftime('%Y-%m-%d')


if __name__ == "__main__":
    try:
        my_day_interval = int(input("Введите количество дней от текущей даты: "))
    except ValueError:
        my_day_interval = 1
    print(calculate_date(my_day_interval))









