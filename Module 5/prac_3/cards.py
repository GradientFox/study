from itertools import combinations
import csv


deck = [i for i in range(1, 53)]

n = int(input("Сколько карт нужно взять?: "))
with open("data.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(combinations(deck, n))
