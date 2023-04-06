from inputkey import input_int, input_float


class Road:
    mas1_in_asphalt = 0
    thick_in_asphalt = 0

    def __init__(self):
        self.__length = input_int('Введите длину дороги, в метрах: ')
        self.__width = input_int('Введите ширину дороги, в метрах: ')

    def asphalt_mass(self, mas1_in_asphalt, thick_in_asphalt):
        x = int(self.__width * self.__length * mas1_in_asphalt * thick_in_asphalt)
        x = x / 1000 if x > 1000 else x
        print('%.2f' % x + 'т')


new_road = Road()
mas1_asphalt = input_float('Введите массу асфальта, в кг, для площади 1кв.м и толщиной в 1 см: ')
thick_asphalt = input_float('Введите толщину асфальта, в метрах: ')
new_road.asphalt_mass(mas1_asphalt, thick_asphalt)
