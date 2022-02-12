from functools import wraps


def val_checker(sub_func):

    def _val_checker(func):
        @wraps(func)
        def wr_func(ch):
            if sub_func(ch):
                return func(ch)
            else:
                raise ValueError(f'wrong arg: {ch}')
        return wr_func

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


try:
    print(calc_cube(-4))
except ValueError as err:
    print(err)
