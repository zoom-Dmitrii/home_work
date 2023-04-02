print('НУжно вводить числа от 0 до 1000')
sum1 = int(-1)
composit = int(-1)
while sum1 < 0 or composit < 0:
    try:
        sum1 = int(input('Введите сумму двух положительных чисел: '))
        composit = int(input('Введите произведение этих же чисел: '))
    except ValueError:
        print("Нужно ввести число")
find = False
if sum1 == 0 and composit == 0:
    print('Первое и второе числа - 0')
else:     
    for i in range(1, sum1 + 1):
        if find == True:
            continue
        for j in range(composit + 1):
            if i + j == sum1 and i * j == composit:
                print(f'Придуманы числа -  {i} и {j}')
                find = True
                continue
    if i == sum1 and j == composit:
        print('Вы ввели несвязанные числа')