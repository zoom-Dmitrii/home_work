'''
Операции над двумя числами.
Числа и знак операции вводятся пользователем.
'''
from inputkey import input_int, input_sign


def operation(answer=''):
    sign = input_sign('Введите операцию (+, -, *, / или 0 для выхода): ')
    if sign == '0':
        answer = 'Завершено'
    elif sign in ['*', '/', '+', '-', '0']:
        num1 = input_int('Ведите первое число: ')
        num2 = input_int('Ведите второе число: ')
        match sign:
            case '*':
                answer = str(num1 * num2)
            case '/':
                try:
                    answer = str(num1 / num2)
                except ZeroDivisionError:
                    answer = 'Ошибка. Деление на ноль'
            case '+':
                answer = str(num1 + num2)
            case '-':
                answer = str(num1 - num2)
        print(f'Результат: {answer}')
        operation(sign)
    return answer


print('Операции над двумя числами. \n'
      'Числа и знак операции вводятся пользователем.')
print(f'Результат: {operation()}')
