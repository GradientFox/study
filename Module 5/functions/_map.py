def cubed(x):
    return pow(x, 3)

l1 = [i for i in range(1, 11)]
response = list(map(cubed, l1))
print(response)