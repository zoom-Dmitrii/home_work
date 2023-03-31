'''
Пользователь должен отгадать число не более чем за 10 попыток в диапозоне от 0 до 100
'''
import random

from inputkey import input_natural


def operation(num_in, num_random_in, trying=9):
    if trying == 0:
        return f'Вы потратили 10 попыток и не отгадали число {num_random_in}'
    if num_in == num_random_in:
        return f'Вы отгадали загаднное число {num_random_in}'
    else:
        if num_in > num_random_in:
            print('Выше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
        trying -= 1
        num_in = input_natural('Введите ваше число: ')
        return operation(num_in, num_random_in, trying)


print('Отгадайте число от 0 до 100')
num_random = random.randint(0, 100)
num = input_natural('Введите ваше число: ')
print(operation(num, num_random))
