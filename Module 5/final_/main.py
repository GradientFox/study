import os, json, csv, pprint

DIR_NAME = os.path.dirname(os.path.abspath(__file__))

def read_data(filename):
    file_name = os.path.join(DIR_NAME, filename)
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)

def get_average_score(data):
    average = lambda scores: sum(scores) / len(scores)
    return [(name, average(value["grades"].values())) for name, value in data.items()]

def get_best_student(scores):
    return max(scores, key=lambda item: item[1])

def get_worst_student(scores):
    return min(scores, key=lambda item: item[1])

def find_student(name, data):
    student = data.get(name.capitalize(), "Студент с таким именем не найден")
    if type(student) is dict:
        print(f"""Имя: {name.capitalize()}
Возраст: {student['age']}
Предметы: {student['subjects']}
Оценки: {student['grades']}""", end="\n\n")
        return
    print(student, end="\n\n")

def new_format(data):
    return [{"name": name} | info for name, info in data.items()]

def create_csv_format(data):
    average = lambda scores: sum(scores) / len(scores)
    return [{
        "name": st["name"],
        "age": st["age"],
        "grade": average(st["grades"].values())
    } for st in data]

def write_csv(filename, data):
    file_name = os.path.join(DIR_NAME, filename)
    with open(file_name, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

students = read_data("students_list.json")

avrage_score = get_average_score(students)
print(*[f"Средний балл для студента {name}: {score}" for name, score in avrage_score], sep="\n" , end="\n\n")
best_student = get_best_student(avrage_score)
worst_student = get_worst_student(avrage_score)
print(f"Наилучший студент: {best_student[0]} (Средний балл: {best_student[1]})", end="\n\n")
print(f"Худший студент: {worst_student[0]} (Средний балл: {worst_student[1]})", end="\n\n")
find_student("john", students)
find_student("Lisa", students)

print("Сортировка по среднему баллу:")
sorted_scores = sorted(avrage_score, key=lambda item: item[1], reverse=True)
print(*[f"{student[0]}: {student[1]}" for student in sorted_scores], sep="\n", end="\n\n")

new_students = new_format(students)
# pprint.pprint(new_students)

csv_format_data = create_csv_format(new_students)
write_csv("students.csv", csv_format_data)