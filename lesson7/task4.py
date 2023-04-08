import random

from inputkey import input_matrix


class Matrix:

    def __init__(self, input_data):
        self.input_data = input_data
        for ind_1 in input_data:
            for ind_2 in range(len(ind_1)):
                ind_1[ind_2] = random.randint(0, 101)

    def __str__(self):
        for ind_1 in self.input_data:
            for ind_2 in ind_1:
                print(ind_2, end=" ")
            print('')
        return "-----"

    def __add__(self, other):
        result_matrix = []
        add1 = self.input_data
        add2 = other.input_data
        # result_matrix = [[add1[i][j] + add2[i][j] for j in range
        # (len(add1[0]))] for i in range(len(add1))]

        for in_1 in range(len(add1)):
            new_el = []
            for in_2 in range(len(add1[in_1])):
                new_el.append(add1[in_1][in_2] + add2[in_1][in_2])
            result_matrix.append(new_el)
        return result_matrix


matrix_list = []
new_matrix1 = input_matrix('Введите размер первой матрицы, цифры через пробел: ')
matrix_list.append(Matrix(new_matrix1))
new_matrix2 = input_matrix('Введите размер второй матрицы, цифры через пробел: ')
matrix_list.append(Matrix(new_matrix2))
print('Первая матрица')
print(matrix_list[0])
print('Вторая матрица')
print(matrix_list[1])
matrix_sum = matrix_list[0] + matrix_list[1]
print('Сумма двух матриц')
for ind1 in matrix_sum:
    for ind2 in range(len(ind1)):
        print(ind1[ind2], end=" ")
    print()
