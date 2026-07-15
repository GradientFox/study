import os, json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_data(filename):
    file_path = os.path.join(SCRIPT_DIR, filename)
    with open(file_path, encoding='utf-8') as f:
        return json.load(f)
    
def get_older_students(data):
    old_students = [data[0]]
    for student in data:
        if student["возраст"] > old_students[0]["возраст"]:
            old_students = [student]
        elif student["возраст"] == old_students[0]["возраст"]:
            old_students.append(student)
    return old_students

def get_count_students(data, subject: str):
    count = 0
    for student in data:
        if subject.lower() in [i.lower() for i in student["предметы"]]:
            count += 1
    return count
    
file_name = "students.json"
data = get_data(file_name)
print(f"Количество студентов: {len(data)}")
older = get_older_students(data)
print(f"Старшие студенты: ")
print("\n".join([f"{student["имя"]} - {student["возраст"]} - {student["город"]}" for student in older]))
subject = input("Укажите предмет для проверки количества студентов: ")
count_students = get_count_students(data, subject)
print(f"Количество студентов по предмету {subject}: {count_students}")

