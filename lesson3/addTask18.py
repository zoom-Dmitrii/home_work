'''
Поиск близкого по величине элемента к Х в массиве чисел от 0 до N
'''


def func_find(n1, n2, num_array=[]):
    count = []
    for i in range(n1 + 1):
        print(i, end=' ')
        num_array.append(i)
    print()
    if n2 + 2 > n1:
        return num_array.index(len(num_array) - 1)
    for i in num_array:
        if i == n2 - 1 or i == n2 + 1:
            count.append(i)
    return count


def input_int(out_txt, digit=None):
    while digit is None or digit < 0:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


print('Поиск близкого по величине элемента к Х в массиве чисел от 0 до N')
number1 = input_int('Введите размер массива: ')
number2 = input_int('Введите контрольное число: ')
print(f'Ближайшее к контрольному число:', func_find(number1, number2))
