'''
Функция с рекурсией sum_number(a, b), возвращающая сумму двух целых неотрицательных чисел.
Допускаются операции только +1 и -1
'''

from inputkey import input_natural


def operation(num_a, num_b):
    if num_b == 0:
        return f'Результат: {num_a}'
    else:
        num_a += 1
        num_b -= 1
        return operation(num_a, num_b)


print('Сумма двух целых неотрицательных чисел через операцию +1')
number_a = input_natural('Введите первое число A: ')
number_b = input_natural('Введите второе число B: ')
print(f' A = {number_a}; B = {number_b} -> {operation(number_a, number_b)}')
