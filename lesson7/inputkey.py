'''
Модуль обработки корректного ввода данных
'''
dict_ = {
    0: "\u2070",
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079"
}


def input_int(out_txt, digit=None):
    while digit is None:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit

def input_float(out_txt, digit=None):
    while digit is None:
        try:
            digit = float(input(out_txt, ))
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


def input_natural_range(out_txt, digit=None):
    while digit is None or digit < 1 or digit > 100 :
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести натуральное число")
    return digit


def input_sign(out_txt, sign=None):
    while sign not in ['*', '/', '+', '-', '0']:
        sign = input(out_txt, )
    return sign
