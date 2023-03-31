'''
 Возведение число А в целую степень B с помощью рекурсии
'''
from inputkey import input_int, input_natural


def operation(num_a, num_b, res=1):
    if num_b == 0:
        return f'Результат: {res}'
    else:
        res *= num_a
        num_b -= 1
        return operation(num_a, num_b, res)


print('Возведение число А в целую степень B')
number_a = input_int('Введите число A: ')
number_b = input_natural('Введите степень B: ')
print(f' A = {number_a}; B = {number_b} -> {operation(number_a, number_b)}')
