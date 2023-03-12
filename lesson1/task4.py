
revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
profitability = True 
profit = revenue - costs
worker, worker_prof = int(0), int(0)

if revenue > costs:
    print(f'Финансовый результат - Прибыль. Ее величина: {profit}')
else:
    print(f'Финансовый результат - Убыток. Ее величина: {profit}')
    print('Рентабельность отрицательна')
    profitability =  False
if profitability != False:
    print(f'Рентабельность выручки = {round((profit / costs)*100,2)}%')
while worker < 1:
    worker = int(input('Введите численность сотрудников фирмы: '))
worker_prof = profit / worker
print(f'Прибыль фирмы в расчете на одного сотрудника = {round(worker_prof,2)}')