from functools import reduce


def my_add(a, b):
    print(f'{a} + {b} = {a+b}')
    return a+b


reduce(my_add, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])
