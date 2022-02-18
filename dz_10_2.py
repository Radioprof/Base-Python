from abc import ABC, abstractmethod


class Closes(ABC):
    def __init__(self, size):
        self.size = size

    def __add__(self, other):
        return self.material + other.material

    @abstractmethod
    def material(self):
        pass


class Coat(Closes):

    @property
    def material(self):
        return round((self.size / 6.5 + 0.5), 2)


class Costume(Closes):

    @property
    def material(self):
        return round((self.size * 2 + 0.3), 2)


a = Coat(48)
print(a.material)
b = Costume(1.76)
print(b.material)
c = Coat(52)
print(c.material)
print(a.material + b.material * 2 + a.material + c.material)
