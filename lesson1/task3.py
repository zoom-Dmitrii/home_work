print('Выод суммы в виде n + nn + nnn + ...')
number = int(0)
while number < 1 or number > 9:
    number = int(input('Введите число n от 1 до 9: '))

num, result = 0, ''
for i in range(1, number + 1):
   num = 0
   for n in range(i):
       num = num + number
   result = result + str(num)
print(result)