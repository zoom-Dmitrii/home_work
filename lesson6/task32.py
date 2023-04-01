'''
Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
'''
import random

from inputkey import input_natural_range


def operation(start, stop, list_el, list_new=[], n=0):
    if n > stop:
        return list_new
    else:
        if start <= n <= stop:
            list_new.append(list_el[n - 1])
        n += 1
        return operation(start, stop, list_el, list_new, n)


print('Ввод диапозона поиска, в пределах от 1 до 100')
first = input_natural_range('Введите начальный индекс диапозона: ')
last = input_natural_range('Введите конечный индекс диапозона: ')
print(f'Массив с произвольными цифрами от 1 до 100')
list_test = [random.randrange(0, 100) for i in range(0, 100)]
print(f'{list_test}')
if first > last:
    ren = last
    last = first
    first = ren
print(f'Числа в диапозоне индексов от {first} до {last}')
print(operation(first, last, list_test))
