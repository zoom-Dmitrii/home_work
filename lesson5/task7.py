'''
Доказательсвто равенства: 1+2+...+n = n(n+1)/2,
'''

from inputkey import input_natural


def operation(num, num_ind=1, left_side='', left_sum=0):
    if num_ind > num:
        return left_side, left_sum
    else:
        if left_side == '':
            left_side = str(num_ind)
        else:
            left_side = left_side + ' + ' + str(num_ind)
        left_sum = left_sum + num_ind
        num_ind += 1
        return operation(num, num_ind, left_side, left_sum)


sign = input_natural('Введите натуральное число: ')
answer = operation(sign)
print(f' {answer[1]} = {int(sign * (sign + 1) / 2)}')
print(f'Доказателсьво ** {answer[0]} = {sign}({sign}+1)/2 ** верно')
