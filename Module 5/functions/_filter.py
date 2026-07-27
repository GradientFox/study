def condition(x):
    return not (x % 5)

l1 = [i for i in range(1, 26)]
response = list(filter(condition, l1))
print(response)