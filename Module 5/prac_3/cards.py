from itertools import combinations
import csv


deck = [i for i in range(1, 53)]
n = None
while n not in deck:
    try:
        n = int(input("Сколько карт нужно взять?: "))
        if n not in deck:
            raise ValueError()
    except Exception as err:
        print("Укажите значение из диапозона 1-52.")

with open("data.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(combinations(deck, n))
