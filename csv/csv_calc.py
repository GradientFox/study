import csv, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data(filename):
    full_path = SCRIPT_DIR + "\\" + filename
    with open(full_path, encoding='utf-8') as f:
        reader = csv.reader(f)
        temp = []
        for row in reader:
            try:
                temp.append(
                    {
                        "Название": row[0],
                        "Количество": int(row[1]),
                        "Цена": int(row[2])
                    }
                )
            except ValueError as err:
                print(err)
                print("Недопустимые символы в графе 'Количество' или 'Цена'")
        return temp

def calc_price(data):
    full_price = 0
    for item in data:
        full_price += item["Количество"] * item["Цена"]
    return full_price


file_name = "prices.csv"
data = get_data(file_name)
price = calc_price(data)
print(price)
