import winter as winter

print('Вывод времени года по введенному месяцу ')
month = 0
winter = [1, 2, 12]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
season = {'Зима': winter, 'Весна': spring, "Лето": summer, "Осень": autumn}

while month < 1 or month > 12:
    try:
        month = int(input('Введите месяц цифрой от 1 до 12: '))
    except ValueError:
        print("Нужно ввести число")

for k, v in season.items():
    if month in v:
        print(k)
        break
