import os, csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data(filename):
    response = []
    full_path = os.path.join(SCRIPT_DIR, filename)
    with open(full_path, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            response.append(line.strip().split('\t'))
    return response

def create_csv(data, filename):
    temp = filename.split('.')
    temp[-1] = "csv"
    full_path = os.path.join(SCRIPT_DIR, ".".join(temp))
    with open(full_path, 'w', encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)

file_name = 'prices.txt'
data = get_data(file_name)
print(data)
create_csv(data, file_name)