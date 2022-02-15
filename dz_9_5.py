class Stationery:
    title = 'Родительский'

    def draw(self):
        print(f'{Stationery.title} метод. Запуск отрисовки')


class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')


class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')


class Handle(Stationery):
    def draw(self):
        print('Рисуем маркером')


a = Stationery()
a.draw()
b = Pencil()
b.draw()
c = Pen()
c.draw()
d = Handle()
d.draw()
