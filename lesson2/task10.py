from random import randrange

count = int(-1)
while count < 0:
    try:
        count = int(input('Введите общее количество монет: '))
    except ValueError:
        print("Нужно ввести число")

print('Высыпали монеты на стол. Что бы все монеты были одной стороной,')
print()
heads = randrange(0, count + 1) # Сторона монеты орел
tails = count - heads           # Сторона монеты решка 
if heads == tails ==0:
    print('Нет монет')
elif heads == 0:
    print('Все монеты уже вверх решкой')
elif tails == 0:
    print('Все монеты уже вверх орлом')
elif heads > tails:
    print(f'нжно перевернуть {tails} шт. решком вверх')
elif tails > heads:
    print(f'нужно перевернуть {heads} шт. орлом вверх')
else:
    print(f'можо перевернуть или {tails} шт. решком вверх \
или {heads} вверх орлом')
print('')
print(f'Для проверки орел {heads} шт., решка {tails} шт')