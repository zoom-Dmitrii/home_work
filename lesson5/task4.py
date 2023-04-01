'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
'''
from inputkey import input_natural


def operation(num, sum_el=1):
    if num == 1:
        return f'Сумма {el} элементов равна: {sum_el}'
    else:
        if num % 2 == 1:
            sum_el = sum_el + sum_el / 2 * -1
        else:
            sum_el = sum_el + sum_el / 2
        num -= 1
        return operation(num, sum_el)


el = input_natural('Введите количество элементов: ')
print(operation(el))
