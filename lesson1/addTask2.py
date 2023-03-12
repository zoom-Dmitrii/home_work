print('Подсчет суммы из цифр числа')
num = input('Введите число: ')
sum = int(0)
for i in num:
    sum = sum + int(i) 
print('Результат: ', sum)