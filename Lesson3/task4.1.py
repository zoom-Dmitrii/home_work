'''
Ввод трех чисел и
поиск суммы из двух максимальных чисел
Через условия функцию sort()
'''


def input_int(out_txt, digit=None):
    while digit is None:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


def func_sum_max(n1, n2, n3, sum_max=[]):
    """Функция поиска суммы из двух максимальных чисел"""
    sum_max[:0] = [n1, n2, n3]
    sum_max.sort()
    sum_max = int(sum_max[2] + sum_max[1])
    return sum_max


print('Ввод трех чисел. Подсчет суммы из двух максимальных чисел')
number1 = input_int('Введите число 1: ')
number2 = input_int('Введите число 2: ')
number3 = input_int('Введите число 3: ')
print(func_sum_max(number1, number2, number3))
