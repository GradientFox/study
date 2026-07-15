import os, json, csv

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_employees(filename):
    file_path = os.path.join(SCRIPT_DIR, filename)
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)

def get_performance(filename):
    file_path = os.path.join(SCRIPT_DIR, filename)
    with open(file_path, encoding="utf-8") as f:
        return list(csv.DictReader(f))
    
def merge_data(emp, perf):
    response = []
    index_pipe = [i["id"] for i in emp]
    for item in perf:
        temp = emp[index_pipe.index(int(item["employee_id"]))]
        temp["производительность"] = item["performance"]
        response.append(temp)
    return response

def get_best_employee(data):
    best = data[0]
    for employee in data:
        if employee["производительность"] > best["производительность"]:
            best = employee
    return best
    

employees = get_employees("employees.json")
performance = get_performance("performance.csv")

data = merge_data(employees, performance)
average_perf = sum(int(item["performance"]) for item in performance) / len(performance)
print(f"Средняя производительность: {average_perf}")
best_employee = get_best_employee(data)
print(f"Лучший работник: {best_employee["имя"]} - {best_employee["производительность"]}")
