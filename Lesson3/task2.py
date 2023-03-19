num1, num2 = None, None


def div_func(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        res = 'Ошибка. Делене на ноль'
    return res


while num1 is None or num2 is None:
    try:
        num1 = int(input('Введите первое число: '))
        num2 = int(input('Введите второе число: '))
    except ValueError:
        print("Нужно ввести число")

print(div_func(num1, num2))
