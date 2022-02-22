class DateDec:
    def __init__(self, dd, mm, yyyy):
        self.day = dd
        self.month = mm
        self.year = yyyy

    @staticmethod
    def valid_d(dd, mm, yyyy):
        if yyyy in range(1900, 2201) and mm in range(1, 13) and dd in range(1, 32):
            pass
        else:
            raise ValueError(f'Не правильный формат даты')

    @classmethod
    def date(cls, str_d):
        dd, mm, yyyy = map(int, str_d.split('.'))
        cls.valid_d(dd, mm, yyyy)
        return cls(dd, mm, yyyy)
        # try:
        #     DateDec.valid_d(dd, mm, yyyy)
        #     return cls(dd, mm, yyyy)
        # except ValueError as f:
        #     return f'{f}'


try:
    a = DateDec.date('30.12.1900')
except ValueError as f:
    print(f'{f}')
else:
    print(f'день - {a.day}, месяц - {a.month}, год - {a.year}')
