'''
Доказательсвто равенства: 1+2+...+n = n(n+1)/2,
'''

from inputkey import input_natural


def operation(num, num_ind=1, left_side='', left_sum=0):
    if num_ind > num:
        print(f' {left_sum} = {int(num * (num + 1) / 2)}')
        return f'Доказателсьво ** {left_side} = {num}({num}+1)/2 ** верно'
    else:
        if left_side == '':
            left_side = str(num_ind)
        else:
            left_side = left_side + ' + ' + str(num_ind)
        left_sum = left_sum + num_ind
        num_ind += 1
        return operation(num, num_ind, left_side, left_sum)


sign = input_natural('Введите натуральное число: ')
print(operation(sign))
