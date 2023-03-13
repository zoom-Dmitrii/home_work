num = 0
tiket_nums = 6
sum1, sum2 = int(0), int(0)
num = input('Введите шестизначный номер билета: ')
while len(num) != tiket_nums:
    num = input('Введите шестизначный номер билета: ') 
sum1 = int(num[0]) + int(num[1]) + int(num[2])
sum2 = int(num[3]) + int(num[4]) + int(num[5])
if sum1 == sum2:
    print(f'{num} -> билет счастливый')
else: 
    print(f'{num} -> билет обычный')