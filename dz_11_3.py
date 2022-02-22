class NonDig(Exception):
    def __init__(self, txt):
        self.txt = txt


a = input('Введите целое число: ')
dig_list = []
while a != 'stop':
    try:
        if (a[0] == '-') and a[1:].isdigit() or a.isdigit():
            pass
        else:
            raise NonDig('Необходимо ввести целое число!')

    except NonDig as err:
        print(err)
    else:
        dig_list.append(int(a))
    finally:
        a = input('Введите целое число: ')
print(dig_list)
