login = input('Задайте Логин: ')
password = input('Задайте пароль: ')
age = int(input('Введите возраст: '))

while age < 0 or age > 110:
    age = int(input('Введите возраст: '))

message = "Доступ разрешен"
if age < 18:
    acess = 0
    message = 'Доступ запрещен'

print('Ваши данные:')
print(f"Логин: {login} || Пароль: {password} || Состояние: {message}")