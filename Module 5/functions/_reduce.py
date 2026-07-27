from functools import reduce

def is_odd(x):
    return x % 2

def multi(x, y):
    return x * y

l1 = [i for i in range(1, 11)]
response = reduce(multi, filter(is_odd, l1))
print(response)