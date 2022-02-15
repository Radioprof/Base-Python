class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        Road._length = length
        Road._width = width

    @staticmethod
    def m_asphalt():
        mass = Road._length * Road._width * 25 * 5
        return mass


road_bd = Road(5, 20)
print(f'Для строительства {road_bd._length}км дороги шириной {road_bd._width}м понадобиться {road_bd.m_asphalt()}т асфальта.')
