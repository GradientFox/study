from collections import deque


data = deque([5, 4, 3])
print(data)
data.append(6)
print(data)
data.appendleft(1)
print(data)
data.extendleft([10, 11])
print(data)
print(data.pop())
print(data.popleft())
print(data)