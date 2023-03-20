print('Вывод времени года по введенному месяцу ')
month = 0
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
season = [winter, spring, summer, autumn]

while month < 1 or month > 12:
    try:
        month = int(input('Введите месяц цифрой от 1 до 12: '))
    except ValueError:
        print("Нужно ввести число")

if season[0].count(month):
    print('Зима')
elif season[1].count(month):
    print('Весна')
elif season[2].count(month):
    print('Лето')
else:
    print('Осень')
