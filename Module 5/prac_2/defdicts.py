from collections import defaultdict

d = defaultdict(list)
d["a"] = [1, 2, 3, 4, 5]
d["b"].extend(["hello", "bye"])
print(d)