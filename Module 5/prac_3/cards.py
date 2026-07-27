from itertools import permutations
import csv


deck = [i for i in range(1, 53)]

n = int(input("Сколько карт нужно взять?: "))
response = list(permutations(deck, n))

print(*response, sep="\n")
with open("data.csv", "w", encoding="utf-8", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(response)
