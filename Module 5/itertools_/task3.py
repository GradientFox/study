from itertools import cycle, chain, islice

l1 = ['a', 'b']
l2 = [1, 2, 3]
l3 = ['x', 'y']

union = cycle(chain(l1, l2, l3))

print(list(islice(union, 15)))