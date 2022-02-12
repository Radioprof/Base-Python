from functools import wraps


def type_logger(func):
    @wraps(func)
    def pr_type(*args):
        res = func(*args)
        print(func.__name__, end=' ')
        for _a in (args):
            print(f'({_a}: {type(_a)})', end=', ')
        return res
    return pr_type


@type_logger
def calc_cube(x, y, z):
    return (x + y + z) ** 3


a = calc_cube(5, 2, 7)
print(f'Result: {a} - {type(a)}')
