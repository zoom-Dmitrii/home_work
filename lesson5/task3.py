'''
 Сформировать из введенного числа обратное по порядку входящих в него цифр
'''
from inputkey import input_natural


def operation(num, num_new=''):
    if num == 0:
        return f'Перевернутое число: {num_new}.'
    else:
        num_new = num_new + str(num % 10)
        return operation(num // 10, num_new)


sign = input_natural('Введите натуральное число: ')
print(operation(sign))
