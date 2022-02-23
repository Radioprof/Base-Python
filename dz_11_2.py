class DivZero(Exception):
    def __init__(self, txt):
        self.txt = txt


a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
try:
    if b == 0:
        raise DivZero('На 0 делить нельзя')

except DivZero as err:
    print(err)
else:
    c = a / b
    print(f'Частное: {c}')