# Задание 1
l1 = ["apple", "kiwi", "banana", "fig"]
filtered = list(filter(lambda x: len(x) > 4, l1))
print(f"Болшье 4 символов: {', '.join(filtered)}", end="\n\n")

# Задание 2
studentds = [{"name": "John", "grade": 90}, {"name": "Jane", "grade": 85}, {"name": "Dave", "grade": 92}]
smartest = max(studentds, key=lambda student: student["grade"])
print(f"Наивысший балл у {smartest["name"]} - {smartest["grade"]}", end="\n\n")

# Задание 3
data = [
    (1, 5),
    (3, 2),
    (2, 8),
    (4, 3)
]
response = sorted(data, key=lambda x: sum(x))
print(response, end="\n\n")

# Задание 4
l2 = [i for i in range(1, 11)]
even_nums = list(filter(lambda x: not x % 2, l2))
print(f"Четные числа: {' '.join(map(lambda x: str(x), even_nums))}", end="\n\n") # Только лишь забавы ради xD Все делаем через лямбду

# Задание 5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}, возвраст {self.age}"

l3 = [
    Person("Misha", 22),
    Person("Nikita", 31),
    Person("Alex", 15),
    Person("Artem", "19")
]
sorted_people = sorted(l3, key=lambda person: int(person.age))
print(*sorted_people, sep="\n")