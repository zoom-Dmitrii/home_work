num = 0
tiket_nums = 6
sum1, sum2 = int(0), int(0)
num = input('Введите шестизначный номер билета: ')
while len(num) != tiket_nums:
    num = input('Введите шестизначный номер билета: ') 
for i in range(int(len(num)/2)):
    sum1 = sum1 + int(num[i])
    sum2 = sum2 + int(num[len(num)-1-i])
if sum1 == sum2:
    print(f'{num} -> билет счастливый')
else: 
    print(f'{num} -> билет обычный')