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


def input_salary(out_txt, digit=None):
    while digit is None or digit < 0:
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


def input_matrix(out_txt, matrix=[], line_matrix=None, column_matrix=None):
    matrix = []
    while line_matrix is None or column_matrix is None or line_matrix < 1 or column_matrix < 1:
        try:
            read_data = input(out_txt, ).split(' ')
            line_matrix = int(read_data[0])
            column_matrix = int(read_data[1])
        except ValueError:
            print("Нужно ввести корректный размер матрицы")
        except IndexError:
            print("Нужно ввести корректный размер матрицы")
    for ind_1 in range(line_matrix):
        new_el = []
        for ind_2 in range(column_matrix):
            new_el.append(0)
        matrix.append(new_el)
    return matrix
