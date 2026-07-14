import csv, os, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data(filename) -> dict:
    file_path = os.path.join(SCRIPT_DIR, filename)
    with open(file_path, encoding='utf-8') as f:
        return {key:value.strip() for key, value in csv.reader(f, delimiter=',', )}


file_name = "данные.csv"
data = get_data(file_name)
json_data = json.dumps(data, ensure_ascii=False, indent=4)
print(json_data)
