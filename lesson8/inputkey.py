'''
Модуль обработки корректного ввода данных
'''
from datetime import datetime


def input_int(out_txt, digit=None):
    while digit is None:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


def input_float(out_txt, digit=None):
    while digit is None or digit < 1:
        try:
            digit = float(input(out_txt, ))
        except ValueError:
            print("Нужно реальную цену")
    return digit


def input_natural(out_txt, digit=None):
    while digit is None or digit < 1:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести актуальное число товара")
    return digit


def input_natural_range(out_txt, digit=None):
    while digit is None or digit < 1 or digit > 100:
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


def get_date():
    now = datetime.now()
    return f'{now.day}.{now.month}.{now.year} {now.hour}:{now.minute}'


#  Ввод даты в формате число.месяц.год"
#  Если время не указать, проставит 00:00
def input_date(out_txt, date_in=''):
    while date_in == '':
        try:
            date_in = datetime.strptime(input(out_txt, ), '%d.%m.%Y')
        except ValueError:
            print("Нужно ввести дату в формате число.месяц.год")
    return date_in
