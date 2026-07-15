import csv, os
from collections import Counter

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data(filename):
    file_path = os.path.join(SCRIPT_DIR, filename)
    with open(file_path, encoding="utf-8") as f:
        return list(csv.DictReader(f))

def get_top_sale(data):
    items = [item["Продукт"] for item in data] 
    count_items = Counter(items)
    return max(count_items, key=count_items.get)

def separate_by_months(data):
    response = {}
    for item in data:
        month = item["Дата"].split("-")[1]
        if not response.get(month):
            response[month] = [item]
        else:
            response[month].append(item)
    return response

def get_sum(data):
    return sum(int(sale["Сумма"]) for sale in data)


file_name = "sales.csv"
data = get_data(file_name)
sum_ = sum(int(sale["Сумма"]) for sale in data)
print(f"Сумма продаж: {sum_}")
popular_item = get_top_sale(data)
print(f"Наибольший объем продаж: {popular_item}")
month_stat = separate_by_months(data)
print("Сумма продаж в месяцах: ")
print("\n".join([f"{month} - {str(get_sum(data))}" for month, data in month_stat.items()]))
