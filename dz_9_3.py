class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {}

    def __init__(self, name, surname, position, income1, income2):
        Worker.name = name
        Worker.surname = surname
        Worker.position = position
        Worker._income['wage'] = income1
        Worker._income['bonus'] = income2


class Position(Worker):

    @staticmethod
    def get_full_name():
        return f'{Worker.name} {Worker.surname}, {Worker.position}'

    @staticmethod
    def get_total_income():
        tot_in = 0
        for i in Worker._income.values():
            tot_in += i
        return tot_in


a = Position('Ivan', 'Kovalev', 'eng.', 40000, 10000)
print(a.get_full_name())
print(f'Доход - {a.get_total_income()}руб.')
