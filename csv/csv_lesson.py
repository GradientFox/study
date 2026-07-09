import csv, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
full_path = SCRIPT_DIR + "\\данные.csv"
with open(full_path, encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


data = [
    {'Имя': 'Анна', 'Возраст': '25', 'Город': 'Москва'},
    {'Имя': 'Петр', 'Возраст': '30', 'Город': 'Санкт-Петербург'},
    {'Имя': 'Мария', 'Возраст': '28', 'Город': 'Киев'}
]

file_name = SCRIPT_DIR + '\\данные_заголовки.csv'

with open(file_name, 'w', encoding="utf-8", newline='') as f:
    field_names = data[0].keys()
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(data)

with open(file_name, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Имя'], row['Возраст'], row['Город'])