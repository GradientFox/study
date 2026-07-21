from collections import deque


# class Queue:
#     def __init__(self):
#         self.data = deque()

#     def size(self):
#         return len(self)
    
#     def is_empty(self):
#         return self.size() == 0

#     def push(self, item):
#         self.data.append(item)
    
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("Queue is empty")
#         return self.data.pop()
    
#     def clear(self):
#         self.data.clear()

def push(data: deque, item):
    data.append(item)

def pop(data: deque):
    return data.pop()

    
d = deque()
push(d, 1)
push(d, 2)
push(d, 3)
print(d)
print(pop(d)) 
print(d)
