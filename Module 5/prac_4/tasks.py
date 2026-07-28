# Задание 1
students_dict = {
    'Саша': 27,
    'Кирилл': 52,
    'Маша': 14,
    'Петя': 36,
    'Оля': 43,
}

print(sorted(students_dict.items(), key=lambda x: x[1]), end="\n\n")

# Задание 2
data = [
    (82, 191),
    (68, 174),
    (90, 189),
    (73, 179),
    (76, 184),
]
print(sorted(data, key=lambda item: item[0] / pow(item[1], 2)), end="\n\n")

# Задание 3
students_list = [
    {
        "name": "Саша",
        "age": 27,
    },
    {
        "name": "Кирилл",
        "age": 52,
    },
    {
        "name": "Маша",
        "age": 14,
    },
    {
        "name": "Петя",
        "age": 36
    },
    {
        "name": "Оля",
        "age": 43,
    }
]
younger = min(students_list, key=lambda student: student["age"])
print(f"{younger['name']} - {younger['age']}")