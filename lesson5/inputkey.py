'''
Модуль обработки корректного ввода данных
'''


def input_int(out_txt, digit=None):
    while digit is None:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


def input_natural(out_txt, digit=None):
    while digit is None or digit < 1:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести натуральное число")
    return digit


def input_sign(out_txt, sign=None):
    while sign not in ['*', '/', '+', '-', '0']:
        sign = input(out_txt, )
    return sign


def input_txt(out_txt, text=''):
    while text == '':
        text = input(out_txt, )
    return text
