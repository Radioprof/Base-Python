class CompNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        if self.b > 0:
            return f'{self.a}+{self.b}j'
        else:
            return f'{self.a}{self.b}j'

    def __add__(self, other):
        return CompNum((self.a + other.a), (self.b + other.b))

    def __mul__(self, other):
        return CompNum((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))


num_1 = CompNum(3, -5)
num_2 = CompNum(4, 7)
print(f'Сумма комплексных чисел = {num_1 + num_2}')
print(f'Произведение комплексных чисел = {num_1 * num_2}')
