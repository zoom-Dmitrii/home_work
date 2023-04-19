'''
Реализовать метакласс. позволяющий создавать всегда один и тот же объект класса
Код основан на первом уроке, с добавлением проверки логированием для температуры,
проверки типа передаваемых данных.

И в строках 79-80, меняя коммент строк, можно проверить разный принцип создания классов
'''
class TestInputSalary:
    class TestInputTxt:
        def __set_name__(self, owner, my_attr):
            self.my_attr = my_attr

        def __set__(self, instance, value):  # Проверки на тип и на непустое значение
            while value == '':
                value = input('Введите текст: ', )
            instance.__dict__[self.my_attr] = value


class TestInputDistance:
    def __init__(self, type_name):
        self.type = type_name

    def __set__(self, instance, value):  # Если пришло корректное значение будет только
        if not isinstance(value, self.type) or value < 0:  # проверка на соответствие типу. Иначе проверка
            instance.__dict__[self.my_attr] = int(0)
        else:
            instance.__dict__[self.my_attr] = value  # через конвертацию

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class TestInputTemperature:
    def __init__(self, type_name):
        self.type = type_name

    def __set__(self, instance, value):
        while not isinstance(value, self.type):
            try:
                value = int(input(f'Значение должно быть корректным: '))
            except ValueError:
                print('Введите температуру')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class MetaPlanet(type):  # Метакласс, создает всегда один класс по первым переданным данным

    def __init__(self, *args, **kwargs):
        print('__init__ in Metaclass. ', self, args, kwargs)  # Печать иницифлизация для отметки
        self.__instance = None
        super().__init__(*args, **kwargs)  # передаются данные класса при инициализации

    '''
    Создание класса через проверку, если раннее был создан класс,
    то создаеся класс с параметрами от первой инициализации
    '''

    def __call__(self, *args, **kwargs):
        print('__call__ in Metaclass')  # Печать вызов для отметки
        print(' ', self, args, kwargs)
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


'''
ниже две строки создания класса
1 - с обработкой метаклассом и создание однотипных классов
2 - обчное создание классов 
для проверки нужно менять коммент на строке создания класса
'''


class PlanetarSystem(metaclass=MetaPlanet):
    # class PlanetarSystem:
    __life = ''  # возможность наличия жизни
    name = TestInputSalary()
    star_system = TestInputSalary()
    distance_to_star_min = TestInputDistance(int)
    distance_to_star_max = TestInputDistance(int)
    temperature = TestInputTemperature(int)

    def __init__(self, name, star_system, distance_to_star_min, distance_to_star_max, temperature):
        self.name = name  # название
        self.star_system = star_system  # принадлежность к звездной системе
        self.distance_to_star_min = distance_to_star_min  # расстояние до звезды минимум
        self.distance_to_star_max = distance_to_star_max  # расстояние до звезды минимум
        self.temperature = temperature  # найденная комфортная температура
        self.__life = self.set_life()

    def set_life(self):
        if -20 < self.temperature < 60:
            return 'жизнь возможна'
        else:
            return 'жизнь НЕ возможна'

    def __str__(self):
        return f'Планета: {self.name}\n' \
               f'Звездная система: {self.star_system}\n' \
               f'Расстояние до звезды минимум: {self.distance_to_star_min} км\n' \
               f'Расстояние до звезды максимум: {self.distance_to_star_max} км\n' \
               f'Наличие комфортной температуры: {self.temperature} С\n' \
               f'Возможность наличия жизни: {self.__life}'


planet_list = []
new_planet = PlanetarSystem('Земля', 'Солнечная', 107_476_259, 152_095_556, 20)
planet_list.append(new_planet)
new_planet = PlanetarSystem('Марс', 'Солнечная', 108_208_930, 152_095_556, 462)
planet_list.append(new_planet)
for p in planet_list:
    print(p for p in planet_list)
    print('---------------------')
print(planet_list[0] is planet_list[1])
print("----------- Созданные классы - ссылки для сравнения --------------")
print(planet_list)
