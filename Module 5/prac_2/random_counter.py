import random
from collections import Counter

def get_random_data():
    return [random.randint(1, 10) for i in range(random.randint(20, 30))]

def get_popular(data):
    return sorted(data.items(), key=lambda x: x[1], reverse=True)[:3]

data = get_random_data()
print(data)
counted = Counter(data)
top_three = get_popular(counted)
print("Самые популярные варианты: ")
print("\n".join([f"Число {item[0]} встречается {item[1]} раз" for item in top_three]))