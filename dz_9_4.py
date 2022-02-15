import random


class Car:

    def __init__(self, speed, color, name, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.police = police

    def go(self):
        print('Автомобиль начал движение')

    def stop(self):
        print('Автомобиль остановился')

    def turn(self):
        rotate = random.choice(['лево', 'право'])
        print(f'Автомобиль {self.name}, {self.color} цвета повернул на{rotate}')

    def show_speed(self):
        return f'Скорость автомобиля - {self.speed}'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'Автомобиль {self.name}, цвет - {self.color} превысил скорость 60км/ч'
        else:
            return f'Скорость автомобиля {self.name}, цвет - {self.color}  - {self.speed}'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'Автомобиль превысил скорость 40км/ч'
        else:
            return f'Скорость автомобиля - {self.speed}'


class Police(Car):
    Car.police = True
    def show_speed(self):
        return f'Скорость автомобиля - {self.speed}. Уступите дорогу полицейской машине!'


a = TownCar(80, 'grey', 'BMW', False)
a.go()
a.turn()
print(a.show_speed())
b = WorkCar(40, 'whait', 'Газель', False)
b.go()
b.turn()
print(b.show_speed())
c = SportCar(160, 'red', 'Mazda', False)
c.go()
c.turn()
print(c.show_speed())
d = Police(160, 'silver', 'Audi', True)
d.go()
d.turn()
print(d.show_speed())
