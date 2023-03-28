'''
Вывод упорядоченных чисел взятых из двух множеств, состоящих из неупорядоченных наборов чисел
'''


def input_int(out_txt, digit=None):
    while digit is None or digit < 1:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


def input_list(out_txt, num, string_in=None):
    while string_in is None or len(string_in) != num or res is False:
        string_in = input(out_txt, )
        string_in = string_in.split()
        res = all(map(str.isdigit, string_in))
    return string_in


def func_join(list_in1, list_in2):
    list_in1.extend(list_in2)
    list_in1 = list(set(list_in1))
    list_in1 = sorted(list_in1, key=lambda x: int(x[0:]))
    return list_in1


print('Вывод упорядоченных чисел взятых из двух множеств, состоящих из неупорядоченных наборов чисел')
print()
# tt = [5, 3, 6, 7, 8, 23, 34, 51, 55, 71, 3, 23, 6, 71]
# print(tt)
# print(sorted(tt))
number1 = input_int('Ведите размер первого списка чисел: ')
number2 = input_int('Введите размер второго списка чисел: ')
list1 = input_list('Введите, через пробел, набор чисел для первого множества: ', number1)
list2 = input_list('Введите, через пробел, набор чисел для второго множества: ', number2)

print(f'Объединенные неповторяющиеся числа:', func_join(list1, list2))
