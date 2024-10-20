from numpy.ma.core import multiply


def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5, 6))
def calculate(n, **kwargs):
    print(kwargs)
    """for (key,value) in kwargs.items():
        print(key)
        print(value)"""
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=7, multiply=8)

