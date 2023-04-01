'''
Заполните массив элементами арифметической прогрессии
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d
'''

from inputkey import input_natural, input_int


def operation(first, d, n, list_el=[]):
    if n == 0:
        return list_el
    else:
        list_el.insert(0, (first + (n - 1) * d))
        n -= 1
        return operation(first, d, n, list_el)


num1 = input_int('Введите первый элемент: ')
num_n = input_natural('Введите количество элементов: ')
step1 = input_int('Введите шаг прогрессии: ')
print(f'Массив элементов арифметической прогрессии \n'
      f'{operation(num1, step1, num_n)}')
