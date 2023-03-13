print('Подсчет суммы из цифр числа')
num = input('Введите число: ')
res = int(0)
for i in num:
    res = res + int(i) 
print('Результат: ', res)