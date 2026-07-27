from itertools import cycle, chain

l1 = ['a', 'b']
l2 = [1, 2, 3]
l3 = ['x', 'y']
count = 0
response = []

for item in cycle(chain(l1, l2, l3)):
    response.append(item)
    count += 1
    if count > 15:
        break

print(response)