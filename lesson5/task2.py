'''
Подсчитать четные и нечетные цифры введенного натурального числа
'''
from inputkey import input_natural


def operation(num, even=0, uneven=0):
    if num == 0:
        return f'Четных цифр: {even}. Нечетных цифр: {uneven}'
    else:
        if num % 2 == 0:
            even += 1
        else:
            uneven += 1
        return operation(num // 10, even, uneven)


#    return f'Четных цифр: {even}. Нечетных чисел: {uneven}'

sign = input_natural('Введите натуральное число: ')
print(operation(sign))
