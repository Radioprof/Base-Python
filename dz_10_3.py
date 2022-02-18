class Cell:
    def __init__(self, num):
        self.cell_num = num

    def __str__(self):
        return f'{self.cell_num}'

    def __add__(self, other):
        return Cell(self.cell_num + other.cell_num)

    def __sub__(self, other):
        if self.cell_num > other.cell_num:
            return Cell(self.cell_num - other.cell_num)
        else:
            return f'Первая клетка меньше второй'

    def __mul__(self, other):
        return Cell(self.cell_num * other.cell_num)

    def __floordiv__(self, other):
        if other.cell_num > 0:
            return Cell(self.cell_num // other.cell_num)
        else:
            return f'Недопустимая длина второй клетки'

    def make_order(self, n):
        self.line = n
        if (self.cell_num % self.line) == 0:
            return f'{"*" * self.line}\n' * int(self.cell_num / self.line)
        else:
            str_cell = f'{"*" * self.line}\n'
            return f'{str_cell* (self.cell_num // self.line)}{"*" * (self.cell_num % self.line)}'


a = Cell(21)
b = Cell(12)
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a.make_order(10))
