from itertools import permutations

word = "Python"

for item in permutations(word):
    print("".join(item))