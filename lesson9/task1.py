# Реализовать дескрипторы для любых двух классов


# Дескриптор проверки текста на соответствие типу str, на не путсую строку
class TestInputTxt:
    def __init__(self, type_name, message=''):  # Принимает в параметрах тип переменной и сообщение
        self.type = type_name  # с нужным текстом вопроса, для повторного ввода
        self.message = message

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr

    def __set__(self, instance, value):  # Проверки на тип и на непустое значение
        while not isinstance(value, self.type):
            input(f'Значение должно быть типа {self.type}', )
        while value == '':
            value = input(self.message, )
        instance.__dict__[self.my_attr] = value


# Проверка цифровых значений зарплата и проценты на тип и логику
class TestInputSalary:
    def __init__(self, type_name, message=''):
        self.type = type_name
        self.message = message

    def __set__(self, instance, value):  # Если пришло корректное значение будет только
        if isinstance(value, self.type):  # проверка на соответствие типу. Иначе проверка
            instance.__dict__[self.my_attr] = value  # через конвертацию
        else:
            test = False
            while not test:
                try:
                    value = float(value)
                    while value < 0:
                        value = float(input(f'{self.message} Значение должно быть корректным: '))
                    test = True
                except ValueError:
                    value = input(f'{self.message} Значение должно быть корректным: ')
            instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr


class Worker:
    __income = {}
    surname = TestInputTxt(str, 'Введите Фамилию: ')
    name = TestInputTxt(str, 'Введите имя: ')
    position = TestInputTxt(str, 'Введите должность: ')
    wage = TestInputSalary(float, 'Оклад: ')
    bonus = TestInputSalary(float, 'Процент: ')

    def __init__(self, surname, name, position, wage, bonus):  # wage - оклад, bonus - премия
        self.name = name
        self.surname = surname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self.__income = {'wage': self.wage, 'bonus': self.bonus}

    def get_income(self):
        if self.__income['bonus'] == 0:
            return self.__income['wage']
        return self.__income['wage'] * (self.__income['bonus'] / 100 + 1)

    def get_wade(self):
        return self.__income['wage']

    def get_bonus(self):
        return str(self.__income['bonus']) + '%'


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return '%.2f' % self.get_income()

    def __str__(self):
        return f'Сотрудник: {self.surname} {self.name}. Должность {self.position}'


print('Ввод данных нового рабочего')
new_surname = input('Введите Фамилию: ')
new_name = input('Введите Имя: ')
new_position = input('Введите должность: ')
new_wage = input('Введите оклад: ')
new_bonus = input('Введите премю (процент от оклада): ')

# Отправка значений идет в текстовом виде, поэтому проверка проходит при преобразовании типов

new_worker = Position(new_surname, new_name, new_position, new_wage, new_bonus)
print(f'{new_worker} | Зарплата: {new_worker.get_total_income()}')
