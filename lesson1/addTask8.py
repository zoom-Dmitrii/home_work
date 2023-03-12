input_data = input('Введите размер шоколадки по длине и ширене, через пробел: ').split()
n = int(input_data[0])
m = int(input_data[1])
k = int(input('Сколько кубиков хотите отломить: '))
if (k % n == 0 or k % m == 0) and k < n * m:
    print('Можно ровно отломить')
else:
    print('Ровно нельзя отломить')