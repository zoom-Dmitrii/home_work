'''
Ввод трех чисел и
поиск суммы из двух максимальных чисел
Через условия if - else
'''


def input_int(out_txt, digit=None):
    while digit is None:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


def func_sum_max(n1, n2, n3):
    """Функция поиска суммы из двух максимальных чисел"""
    sum_max = int(0)
    if n1 > n2:
        sum_max = n1
        if n2 > n3:
            sum_max += n2
        else:
            sum_max += n3
    elif n2 > n3:
        sum_max = n2
        if n1 > n3:
            sum_max += n1
        else:
            sum_max += n3
    else:
        sum_max = n3
        if n1 > n2:
            sum_max += n1
        else:
            sum_max += n2
    return sum_max


number1 = input_int('Введите число 1: ')
number2 = input_int('Введите число 2: ')
number3 = input_int('Введите число 3: ')
print(func_sum_max(number1, number2, number3))
