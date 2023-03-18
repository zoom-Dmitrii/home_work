num = int(-1)
while num < 0:
    try:
        num = int(input('Введите плоложительное число: '))
    except ValueError:
        print("Нужно ввести число")
print(f'Все целые степени двойки до числа {num}')
degree = 0
while 2 ** degree < num:
    degree += 1
    print(f'2^{degree} = {2 ** degree}   ', end = ' ')