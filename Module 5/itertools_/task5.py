from itertools import product
import csv

l1 = ["red", "blue"]
l2 = ["shirt", "shoes"]
response = []
for item in product(l1, l2):
    print(item)
    response.append(item)
    
with open("data.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(response)
