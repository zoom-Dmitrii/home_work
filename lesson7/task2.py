# Задача 2
from inputkey import input_int, input_float


class Road:
    mas1_asphalt = int
    thick_asphalt = int

    def __init__(self, __length, __width):
        self.__length = __length
        self.__width = __width

    def asphalt_mass(self):
        x = int(self.__width * self.__length * self.mas1_asphalt * self.thick_asphalt)
        x = x / 1000 if x > 1000 else x
        print('%.2f' % x + 'т')


length_road = input_int('Введите длину дороги, в метрах: ')
width_road = input_int('Введите ширину дороги, в метрах: ')
new_road = Road(length_road, width_road)
new_road.mas1_asphalt = input_float('Введите массу асфальта, в кг, для площади 1кв.м и толщиной в 1 см: ')
new_road.thick_asphalt = input_float('Введите толщину асфальта, в метрах: ')
new_road.asphalt_mass()
