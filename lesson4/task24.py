'''
Нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль
'''
from random import randrange


def input_int(out_txt, digit=None):
    while digit is None or digit < 1:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


def func_score(bush_in):
    berries = []
    for i in range(bush_in):
        berries.append(randrange(1, bush_in))
    print(f'Ягод на кустах: {berries}')
    i, three_bush = 0, 0
    three_bush = max(three_bush, berries[i] + berries[int(bush_in) - 1] + berries[int(bush_in) - 2])
    three_bush = max(three_bush, berries[i] + berries[i + 1] + berries[int(bush_in) - 1])
    for i in range(bush_in - 2):
        three_bush = max(three_bush, berries[i] + berries[i + 1] + berries[i + 2])
    return three_bush


num_bush = input_int('Ведите целое количество кустов: ')
print(f'Максимальное количество ягод собранных за один раз:', func_score(num_bush))
