num = int(input('Введите общее число журавликов: '))
while num % 6 != 0: 
    print('Число не подходит к условию задачи')
    num = int(input('Введите общее число журавликов: '))
petya = serj = int((num / 3) / 2)
katya = num - (petya + serj)
print(f'Сделали журавликов Петя {petya}, Катя {katya} и Сережа {serj}')