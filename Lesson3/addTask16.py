'''
Поиск повторов цифры X в массиве чисел от 0 до N
'''


def func_find(n1, n2, num_array=[]):
    count = int(0)
    for i in range(n1 + 1):
        print(i, end=' ')
        num_array.append(i)
    print()
    for i in num_array:
        test_num = str(i)
        for n in test_num:
            if int(n) == n2:
                count += 1
    return count


def input_int(out_txt, digit=None):
    while digit is None or digit < 0:
        try:
            digit = int(input(out_txt, ))
        except ValueError:
            print("Нужно ввести число")
    return digit


print('Поиск повторов цифры X в массиве чисел от 0 до N')
number1 = input_int('Введите размер массива: ')
number2 = input_int('Введите искомое число: ')
print(f'Цифра {number2} всчтречается ', func_find(number1, number2), ' раз(а)')
