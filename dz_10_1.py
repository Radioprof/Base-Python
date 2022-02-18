class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(' '.join(map(str, i)) for i in self.matrix)

    def __add__(self, other):
        if len(self.matrix) == len(other.matrix):
            for i in range(len(self.matrix)):
                if len(self.matrix[i]) == len(other.matrix[i]):
                    for j in range(len(self.matrix[i])):
                        self.matrix[i][j] += other.matrix[i][j]
            return Matrix(self.matrix)
        else:
            return f'Матрицы не совпадают по размерности'


a = [[2, 3], [4, 5], [6, 7]]
b = [[5, 2], [0, 7], [7, 5]]
c = Matrix(a)
d = Matrix(b)
print(c)
e = c + d
print(e)
