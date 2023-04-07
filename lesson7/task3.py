# Задание 3

from inputkey import input_salary, input_txt


class Worker:
    __income = {}

    def __init__(self, surname, name, position, wage, bonus):  # wage - оклад, bonus - премия
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': wage, 'bonus': bonus}

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
        return f"Сотрудник: {self.surname} {self.name}"


worker_list = []
input_data = False
print('Ввод данных нового рабочего')
while str.lower(input('Для продолжения введите "да": ')) == 'да':
    input_data = True
    new_name = input_txt('Введите Фамилию: ')
    new_surname = input_txt('Введите имя: ')
    new_position = input_txt('Введите должность: ')
    new_wage = input_salary('Введите оклад: ')
    new_bonus = input_salary('Введите премю (процент от оклада): ')
    new_worker = Position(new_surname, new_name, new_position, new_wage, new_bonus)
    worker_list.append(new_worker)

if input_data:
    print('\n')
    print('Вывод данных по рабочим, полные данные \n')
    for wk in worker_list:
        print(f'{wk} | Зарплата: {wk.get_total_income()}')
    print('------------------ \n')
    print('Каждый параметр отдельно \n')
    for wk in worker_list:
        print(f'Фамилия: {wk.surname}')
        print(f'Имя: {wk.name}')
        print(f'Должность: {wk.position}')
        print(f'Полное имя: {wk.get_full_name()}')
        print(f'Оклад: {wk.get_wade()}')
        print(f'Премия: {wk.get_bonus()}')
        print(f'Полная зарплата: {wk.get_total_income()}')
        print('------------------ \n')
