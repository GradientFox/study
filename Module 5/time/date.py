from datetime import datetime

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

curent_date = datetime.now()
print(curent_date)
print(curent_date.isoweekday(), " - ", curent_date.strftime("%A"))
print("Високосный" if is_leap(curent_date.year) else "Не високосный")


user_date = input("Укажите дату в формате 'ГГГГ-ММ-ДД': ")
delta = datetime.strptime(user_date, "%Y-%m-%d") - datetime.now()
print(f"До даты: {delta.days} дней")
# print(delta) выведет дни и время, но будут также указаны секунды и милисекунды
print(f"{delta.days} дней {delta.seconds // 3600}:{delta.seconds % 3600 // 60}")