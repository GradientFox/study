from itertools import count, islice

def fib():
    a, b = 0, 1
    for _ in count():
        yield a
        a, b = b, a + b

print(list(islice(fib(), 10)))